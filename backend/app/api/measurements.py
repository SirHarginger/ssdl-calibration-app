from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ...database.db import get_db
from ...models.measurement import Measurement
from ...schemas.measurement import MeasurementCreate, MeasurementResponse
from ...services.calculations import calculate_calibration_factor
from fastapi_users import FastAPIUsers
from ...models.user import User
from ...utils.auth import auth_backend, user_manager

router = APIRouter(prefix="/measurements", tags=["measurements"])

fastapi_users = FastAPIUsers[User, int](user_manager, [auth_backend])
current_user = fastapi_users.current_user()

@router.post("/", response_model=MeasurementResponse)
def create_measurement(
    measurement: MeasurementCreate,
    db: Session = Depends(get_db),
    user: User = Depends(current_user)
):
    # Calculate corrected dose and calibration factor
    result = calculate_calibration_factor(measurement, db)
    
    db_measurement = Measurement(
        calibration_id=measurement.calibration_id,
        ssd=measurement.ssd,
        ref_dose_rate_msv_h=result["ref_dose_rate_msv_h"],
        measured_dose=measurement.measured_dose,
        measured_dose_unit=measurement.measured_dose_unit,
        irradiation_time_min=measurement.irradiation_time_min,
        ref_dose_msv=result.get("ref_dose_msv"),
        corrected_dose=result["corrected_dose"],
        calibration_factor=result["calibration_factor"],
        background_measurements=measurement.background_measurements,
        source_on_measurements=measurement.source_on_measurements,
        avg_background=result["avg_background"],
        avg_source_on=result["avg_source_on"]
    )
    db.add(db_measurement)
    db.commit()
    db.refresh(db_measurement)
    return db_measurement