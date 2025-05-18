from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from ...database.db import Base

class Calibration(Base):
    __tablename__ = "calibrations"
    
    id = Column(Integer, primary_key=True, index=True)
    serial_number = Column(String(50))
    calibration_date = Column(Date)
    unit = Column(String(20))  # 'C/s', 'µSv/h', 'mrem/h', 'accumulated_dose'
    scale_factor = Column(Float, default=1.0)
    initial_temperature = Column(Float)
    initial_pressure = Column(Float)
    initial_humidity = Column(Float)
    final_temperature = Column(Float)
    final_pressure = Column(Float)
    final_humidity = Column(Float)
    company_id = Column(Integer, ForeignKey("companies.id"))
    year = Column(Integer)
    user_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime, default=func.now())
    
    company = relationship("Company")
    measurements = relationship("Measurement", back_populates="calibration")