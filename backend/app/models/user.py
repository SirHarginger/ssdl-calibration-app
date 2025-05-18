from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from ...database.db import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    email = Column(String(100))
    role = Column(String(20))  # 'tech', 'admin'
    hashed_password = Column(String(255))
    created_at = Column(DateTime, default=func.now())