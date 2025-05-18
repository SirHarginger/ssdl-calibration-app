from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from ...database.db import Base

class Company(Base):
    __tablename__ = "companies"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, index=True)
    created_at = Column(DateTime, default=func.now())