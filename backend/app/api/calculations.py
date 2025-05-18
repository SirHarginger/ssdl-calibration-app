from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ...database.db import get_db
from ...models.calibration import Calibration
from ...models.measurement import Measurement
from ...services.calculations import calculate_calibration_factor
from ...schemas.measurement import MeasurementCreate
from typing import List
from fastapi_users import FastAPIUsers
from ...models.user import User
from ...utils.auth import auth_backend, user_manager

router = APIRouter(prefix="/calculate", tags=["calculations"])

fastapi_users = FastAPIUsers[User, int](user_manager, [auth_backend])
current_user = fastapi_users.current_user()

@router.post("/{calibration_id}")
def calculate(calibration_id: int, db: Session = Depends(get_db), user: User = Depends(current_user)):
    calibration = db.query(Calibration).filter(Calibration.id == calibration_id).first()
    if not calibration:
        return {"error": "Calibration not found"}
    
    measurements = db.query(Measurement).filter(Measurement.calibration_id == calibration_id).all()
    results = []
    calibration_factors = []
    
    for measurement in measurements:
        measurement_data = MeasurementCreate(
            calibration_id=measurement.calibration_id,
            ssd=measurement.ssd,
            measured_dose=measurement.measured_dose,
            measured_dose_unit=measurement.measured_dose_unit,
            irradiation_time_min=measurement.irradiation_time_min,
            background_measurements=measurement.background_measurements,
            source_on_measurements=measurement.source_on_measurements
        )
        result = calculate_calibration_factor(measurement_data, db)
        results.append({
            "ssd": measurement.ssd,
            "ref_dose_rate_msv_h": result["ref_dose_rate_msv_h"],
            "corrected_dose": result["corrected_dose"],
            "calibration_factor": result["calibration_factor"],
            "avg_background": result["avg_background"],
            "avg_source_on": result["avg_source_on"]
        })
        calibration_factors.append(result["calibration_factor"])
    
    import numpy as np
    avg_calibration_factor = np.mean(calibration_factors) if calibration_factors else 0
    std_calibration_factor = np.std(calibration_factors) if calibration_factors else 0
    
    return {
        "results": results,
        "average_calibration_factor": avg_calibration_factor,
        "std_calibration_factor": std_calibration_factor
    }