from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session
from ...database.db import get_db
from ...services.import_data import import_excel
from fastapi_users import FastAPIUsers
from ...models.user import User
from ...utils.auth import auth_backend, user_manager

router = APIRouter(prefix="/upload", tags=["upload"])

fastapi_users = FastAPIUsers[User, int](user_manager, [auth_backend])
current_user = fastapi_users.current_user()

@router.post("/")
async def upload_file(file: UploadFile = File(...), db: Session = Depends(get_db), user: User = Depends(current_user)):
    if not file.filename.endswith((".xlsx", ".xls", ".csv")):
        return {"error": "Invalid file format. Use Excel or CSV."}
    
    calibration = await import_excel(file, db, user.id)
    return {"calibration_id": calibration.id, "message": "File uploaded and processed successfully"}