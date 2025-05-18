from pydantic import BaseModel
from typing import Optional, List

class MeasurementBase(BaseModel):
    calibration_id: int
    ssd: float
    measured_dose: float
    measured_dose_unit: Optional[str] = None
    irradiation_time_min: Optional[float] = None
    background_measurements: List[float]
    source_on_measurements: List[float]

class MeasurementCreate(MeasurementBase):
    pass

class MeasurementResponse(MeasurementBase):
    id: int
    ref_dose_rate_msv_h: float
    ref_dose_msv: Optional[float] = None
    corrected_dose: float
    calibration_factor: float
    avg_background: float
    avg_source_on: float
    
    class Config:
        orm_mode = True