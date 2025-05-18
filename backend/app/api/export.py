from fastapi import APIRouter, Depends
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from ...database.db import get_db
from ...services.certificate import generate_certificate
from fastapi_users import FastAPIUsers
from ...models.user import User
from ...utils.auth import auth_backend, user_manager

router = APIRouter(prefix="/export", tags=["export"])

fastapi_users = FastAPIUsers[User, int](user_manager, [auth_backend])
current_user = fastapi_users.current_user()

@router.get("/{calibration_id}")
def export_certificate(calibration_id: int, db: Session = Depends(get_db), user: User = Depends(current_user)):
    file_path = generate_certificate(calibration_id, db)
    return FileResponse(file_path, media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document", filename=f"certificate_{calibration_id}.docx")