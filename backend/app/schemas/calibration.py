from pydantic import BaseModel
from datetime import date
from typing import Optional

class CalibrationBase(BaseModel):
    serial_number: str
    calibration_date: date
    unit: str
    scale_factor: float = 1.0
    initial_temperature: Optional[float] = None
    initial_pressure: Optional[float] = None
    initial_humidity: Optional[float] = None
    final_temperature: Optional[float] = None
    final_pressure: Optional[float] = None
    final_humidity: Optional[float] = None
    company_id: int

class CalibrationCreate(CalibrationBase):
    pass

class CalibrationResponse(CalibrationBase):
    id: int
    year: int
    user_id: int
    
    class Config:
        orm_mode = True