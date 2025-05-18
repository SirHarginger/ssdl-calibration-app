from fastapi import UploadFile
from sqlalchemy.orm import Session
from ...models.calibration import Calibration
from ...models.measurement import Measurement
from ...models.company import Company
import pandas as pd
import os
from datetime import datetime

async def import_excel(file: UploadFile, db: Session, user_id: int):
    # Read Excel file
    df = pd.read_excel(file.file)
    
    # Extract calibration data (assumed structure; adjust based on actual Excel files)
    serial_number = df.get("Serial Number", "Unknown")
    calibration_date = pd.to_datetime(df.get("Calibration Date", datetime.now()))
    unit = df.get("Unit", "µSv/h")
    scale_factor = float(df.get("Scale Factor", 1.0))
    initial_temperature = df.get("Initial Temperature")
    initial_pressure = df.get("Initial Pressure")
    initial_humidity = df.get("Initial Humidity")
    final_temperature = df.get("Final Temperature")
    final_pressure = df.get("Final Pressure")
    final_humidity = df.get("Final Humidity")
    company_name = df.get("Company", "Unknown")
    
    # Get or create company
    company = db.query(Company).filter(Company.name == company_name).first()
    if not company:
        company = Company(name=company_name)
        db.add(company)
        db.commit()
        db.refresh(company)
    
    # Create calibration
    calibration = Calibration(
        serial_number=serial_number,
        calibration_date=calibration_date,
        unit=unit,
        scale_factor=scale_factor,
        initial_temperature=initial_temperature,
        initial_pressure=initial_pressure,
        initial_humidity=initial_humidity,
        final_temperature=final_temperature,
        final_pressure=final_pressure,
        final_humidity=final_humidity,
        company_id=company.id,
        year=calibration_date.year,
        user_id=user_id
    )
    db.add(calibration)
    db.commit()
    db.refresh(calibration)
    
    # Note: Measurement parsing requires actual Excel structure
    # Placeholder: Assume measurements in a table format
    # Add logic to parse SSD, dose, background/source-on, etc.
    measurements = []
    for index, row in df.iterrows():
        measurement = Measurement(
            calibration_id=calibration.id,
            ssd=row.get("SSD"),
            measured_dose=row.get("Measured Dose"),
            measured_dose_unit=row.get("Measured Dose Unit"),
            irradiation_time_min=row.get("Irradiation Time (min)"),
            background_measurements=row.get("Background Measurements", []),
            source_on_measurements=row.get("Source On Measurements", [])
        )
        measurements.append(measurement)

    db.bulk_save_objects(measurements)
    db.commit()

    return calibration