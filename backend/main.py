from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from db import Base, engine, SessionLocal
from models import GlucoseReading

Base.metadata.create_all(bind = engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@app.post("/glucose")
def add_glucose(value: float, db: Session = Depends(get_db)):
    reading = GlucoseReading(glucose = value)
    
    db.add(reading)
    db.commit()

    return reading

@app.get("/glucose/latest")
def get_latest(db: Session = Depends(get_db)):
    return(
        db.query(GlucoseReading)
        .order_by(GlucoseReading.timestamp.desc())
        .first()
    )
    
@app.get("/glucose")
def get_all(db: Session = Depends(get_db)):
    return db.query(GlucoseReading).all()