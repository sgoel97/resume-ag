from fastapi import APIRouter
from fastapi import FastAPI, File, UploadFile
import shutil
from pathlib import Path

router = APIRouter(prefix="/upload", tags=["upload"])


@router.post("/")
async def upload_file(file: UploadFile):
    Path("./app/db/files").mkdir(parents=True, exist_ok=True)
    with open(f"./app/db/files/{file.filename}", "wb") as f:
        shutil.copyfileobj(file.file, f)
    return {"filename": file.filename}


@router.get("/")
async def get_files():
    path = Path("./app/db/files").mkdir(parents=True, exist_ok=True)
    file_names = list(path.glob("*.pdf"))
    return {"files": file_names}