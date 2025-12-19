#routes_files.py (upload + list + serve)



from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Header
from sqlalchemy.orm import Session
from .database import get_db
from . import models, schemas
from .auth import decode_token
from .utils import save_upload




router = APIRouter(prefix="/files", tags=["files"])

def get_current_user(authorization: str | None = Header(default=None), db: Session = Depends(get_db)) -> models.User:
    if not authorization or not authorization.lower().startswith("bearer "):
        raise HTTPException(status_code=401, detail="Missing token")

    token = authorization.split(" ", 1)[1].strip()
    payload = decode_token(token)
    if not payload or "sub" not in payload:
        raise HTTPException(status_code=401, detail="Invalid token")

    user = db.query(models.User).filter(models.User.id == int(payload["sub"])).first()
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    return user

@router.post("/upload")
def upload_file(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    user: models.User = Depends(get_current_user),
):
    try:
        stored_name, mime, path = save_upload(file)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    item = models.FileItem(
        filename=file.filename,
        mime_type=mime,
        path=path,
        owner_id=user.id,
    )
    db.add(item)
    db.commit()
    db.refresh(item)
    return {"message": "Uploaded", "id": item.id}

@router.get("", response_model=list[schemas.FileResponse])
def list_my_files(db: Session = Depends(get_db), user: models.User = Depends(get_current_user)):
    items = db.query(models.FileItem).filter(models.FileItem.owner_id == user.id).order_by(models.FileItem.uploaded_at.desc()).all()
    # url served via /static/<stored_name>
    result = []
    for it in items:
        stored_name = it.path.split("/")[-1].split("\\")[-1]
        result.append({
            "id": it.id,
            "filename": it.filename,
            "mime_type": it.mime_type,
            "uploaded_at": it.uploaded_at,
            "url": f"/static/{stored_name}",
        })
    return result








import os

@router.delete("/{file_id}")
def delete_file(
    file_id: int,
    db: Session = Depends(get_db),
    user: models.User = Depends(get_current_user),
):
    file = (
        db.query(models.FileItem)
        .filter(
            models.FileItem.id == file_id,
            models.FileItem.owner_id == user.id,
        )
        .first()
    )

    if not file:
        raise HTTPException(status_code=404, detail="File not found")

    # delete file from disk
    if os.path.exists(file.path):
        os.remove(file.path)

    # delete from DB
    db.delete(file)
    db.commit()

    return {"message": "File deleted successfully"}

