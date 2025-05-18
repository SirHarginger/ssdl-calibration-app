from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func
from ...database.db import Base

class File(Base):
    __tablename__ = "files"
    
    id = Column(Integer, primary_key=True, index=True)
    calibration_id = Column(Integer, ForeignKey("calibrations.id"))
    file_type = Column(String(20))  # 'datasheet', 'certificate'
    file_path = Column(String(255))
    created_at = Column(DateTime, default=func.now())