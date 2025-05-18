from sqlalchemy import Column, Integer, Float, String, ForeignKey, JSON
from sqlalchemy.orm import relationship
from ...database.db import Base

class Measurement(Base):
    __tablename__ = "measurements"
    
    id = Column(Integer, primary_key=True, index=True)
    calibration_id = Column(Integer, ForeignKey("calibrations.id"))
    ssd = Column(Float)
    ref_dose_rate_msv_h = Column(Float)
    measured_dose = Column(Float)
    measured_dose_unit = Column(String(20))
    irradiation_time_min = Column(Float)
    ref_dose_msv = Column(Float)
    corrected_dose = Column(Float)
    calibration_factor = Column(Float)
    background_measurements = Column(JSON)
    source_on_measurements = Column(JSON)
    avg_background = Column(Float)
    avg_source_on = Column(Float)
    
    calibration = relationship("Calibration", back_populates="measurements")