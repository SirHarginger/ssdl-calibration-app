from ...schemas.measurement import MeasurementCreate
from ...models.calibration import Calibration
from sqlalchemy.orm import Session
from pint import UnitRegistry
import numpy as np
from datetime import datetime

ureg = UnitRegistry()

# Base reference dose rates (mSv/h, 2/11/16)
REF_DOSE_RATES = {
    1.0: 1.8246,
    1.5: 0.823,
    2.0: 0.4637,
    2.5: 0.2986,
    3.0: 0.2105,
    3.5: 0.1546,
    4.0: 0.1204,
    4.5: 0.0963,
    5.0: 0.078
}

def calculate_calibration_factor(measurement: MeasurementCreate, db: Session):
    calibration = db.query(Calibration).filter(Calibration.id == measurement.calibration_id).first()
    if not calibration:
        raise ValueError("Calibration not found")
    
    # Calculate decay-adjusted reference dose rate
    base_date = datetime(2016, 2, 11)
    calibration_date = calibration.calibration_date
    days_elapsed = (calibration_date - base_date).days
    half_life_days = 30.17 * 365.25
    decay_factor = 0.5 ** (days_elapsed / half_life_days)
    ref_dose_rate_msv_h = REF_DOSE_RATES.get(measurement.ssd, 0) * decay_factor
    
    # Calculate averages
    avg_background = np.mean(measurement.background_measurements)
    avg_source_on = np.mean(measurement.source_on_measurements)
    corrected_dose = avg_source_on - avg_background
    
    # Unit conversions
    if calibration.unit == "C/s":
        corrected_dose_µsv_h = corrected_dose  # No conversion needed
        ref_dose_rate_µsv_h = ref_dose_rate_msv_h * 1000
        calibration_factor = (ref_dose_rate_µsv_h * calibration.scale_factor) / corrected_dose_µsv_h if corrected_dose_µsv_h != 0 else 0
        ref_dose_msv = None
    elif calibration.unit == "µSv/h":
        corrected_dose_µsv_h = corrected_dose
        ref_dose_rate_µsv_h = ref_dose_rate_msv_h * 1000
        calibration_factor = (ref_dose_rate_µsv_h * calibration.scale_factor) / corrected_dose_µsv_h if corrected_dose_µsv_h != 0 else 0
        ref_dose_msv = None
    elif calibration.unit == "mrem/h":
        corrected_dose_µsv_h = corrected_dose * 10  # 1 mrem = 10 µSv
        ref_dose_rate_µsv_h = ref_dose_rate_msv_h * 1000
        calibration_factor = (ref_dose_rate_µsv_h * calibration.scale_factor) / corrected_dose_µsv_h if corrected_dose_µsv_h != 0 else 0
        ref_dose_msv = None
    elif calibration.unit == "accumulated_dose":
        # Convert measured dose to dose rate (µSv/h)
        irradiation_time_h = measurement.irradiation_time_min / 60
        if measurement.measured_dose_unit == "mSv":
            measured_dose_µsv = measurement.measured_dose * 1000
        else:  # Assume µSv
            measured_dose_µsv = measurement.measured_dose
        corrected_dose_µsv_h = (corrected_dose * 1000) / irradiation_time_h if irradiation_time_h != 0 else 0
        ref_dose_rate_µsv_h = ref_dose_rate_msv_h * 1000
        ref_dose_msv = ref_dose_rate_msv_h * irradiation_time_h
        calibration_factor = (ref_dose_msv * calibration.scale_factor) / (corrected_dose / 1000) if corrected_dose != 0 else 0
    
    return {
        "ref_dose_rate_msv_h": ref_dose_rate_msv_h,
        "corrected_dose": corrected_dose_µsv_h if calibration.unit != "C/s" else corrected_dose,
        "calibration_factor": calibration_factor,
        "avg_background": avg_background,
        "avg_source_on": avg_source_on,
        "ref_dose_msv": ref_dose_msv
    }