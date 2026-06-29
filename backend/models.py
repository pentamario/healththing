from sqlalchemy import Column, Integer, Float, DateTime
from datetime import datetime

from db import Base

class GlucoseReading(Base):
    __tablename__ = "glucose_readings"
    
    id = Column(Integer, primary_key = True, index = True)
    glucose = Column(Float, nullable = False)
    timestamp = Column(DateTime, default=datetime.utcnow)