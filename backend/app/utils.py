import os, uuid, shutil
from fastapi import UploadFile

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # points to app/
UPLOAD_DIR = os.path.join(BASE_DIR, "uploads")

ALLOWED_MIME = {"image/jpeg", "image/png", "image/webp", "video/mp4", "video/webm"}

def ensure_upload_dir():
    os.makedirs(UPLOAD_DIR, exist_ok=True)

def save_upload(file: UploadFile) -> tuple[str, str, str]:
    if file.content_type not in ALLOWED_MIME:
        raise ValueError("Unsupported file type")

    ensure_upload_dir()

    ext = os.path.splitext(file.filename)[1].lower()
    stored_name = f"{uuid.uuid4().hex}{ext}"
    stored_path = os.path.join(UPLOAD_DIR, stored_name)

    with open(stored_path, "wb") as out:
        shutil.copyfileobj(file.file, out)

    return stored_name, file.content_type, stored_path
