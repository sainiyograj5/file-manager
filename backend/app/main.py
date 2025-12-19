from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pathlib import Path

from .database import Base, engine
from .routes_auth import router as auth_router
from .routes_files import router as files_router

app = FastAPI(title="File Management App")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # lock this down later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

# Serve uploaded files (absolute path)
BASE_DIR = Path(__file__).resolve().parent  # app/
upload_dir = BASE_DIR / "uploads"
upload_dir.mkdir(exist_ok=True)

app.mount("/static", StaticFiles(directory=str(upload_dir)), name="static")

app.include_router(auth_router)
app.include_router(files_router)

# @app.get("/")
# def root():
#     return {"data retrived successfullyyyyyyy......"}




# @app.get("/")
# def home():
#     return {
#         "message": "Backend running successfully",
#         "docs": "/docs"
#     }

@app.get("/")
def root():
    return {
        "message": "File Management API is running",
    }
