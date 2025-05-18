from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ...database.db import get_db
from ...models.calibration import Calibration
from ...schemas.calibration import CalibrationCreate, CalibrationResponse
from fastapi_users import FastAPIUsers
from ...models.user import User
from ...utils.auth import auth_backend, user_manager

router = APIRouter(prefix="/calibrations", tags=["calibrations"])

fastapi_users = FastAPIUsers[User, int](user_manager, [auth_backend])
current_user = fastapi_users.current_user()

@router.post("/", response_model=CalibrationResponse)
def create_calibration(
    calibration: CalibrationCreate,
    db: Session = Depends(get_db),
    user: User = Depends(current_user)
):
    db_calibration = Calibration(
        serial_number=calibration.serial_number,
        calibration_date=calibration.calibration_date,
        unit=calibration.unit,
        scale_factor=calibration.scale_factor,
        initial_temperature=calibration.initial_temperature,
        initial_pressure=calibration.initial_pressure,
        initial_humidity=calibration.initial_humidity,
        final_temperature=calibration.final_temperature,
        final_pressure=calibration.final_pressure,
        final_humidity=calibration.final_humidity,
        company_id=calibration.company_id,
        year=calibration.calibration_date.year,
        user_id=user.id
    )
    db.add(db_calibration)
    db.commit()
    db.refresh(db_calibration)
    return db_calibration

@router.get("/{id}", response_model=CalibrationResponse)
def get_calibration(id: int, db: Session = Depends(get_db)):
    calibration = db.query(Calibration).filter(Calibration.id == id).first()
    if not calibration:
        raise HTTPException(status_code=404, detail="Calibration not found")
    return calibration