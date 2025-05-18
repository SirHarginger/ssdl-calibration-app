import pandas as pd
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# Database configuration
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://ssdl_user:ssdl_password@localhost:5432/ssdl_db")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

def import_excel(file_path, user_id=1):
    db = SessionLocal()
    try:
        df = pd.read_excel(file_path)
        # Placeholder parsing (adjust based on actual Excel structure)
        serial_number = df.get("Serial Number", "Unknown")
        calibration_date = pd.to_datetime(df.get("Calibration Date", datetime.now()))
        unit = df.get("Unit", "µSv/h")
        scale_factor = float(df.get("Scale Factor", 1.0))
        company_name = df.get("Company", "Unknown")
        
        # Insert company (simplified)
        company_id = 1  # TODO: Implement company lookup/creation
        
        # Insert calibration
        calibration = {
            "serial_number": serial_number,
            "calibration_date": calibration_date,
            "unit": unit,
            "scale_factor": scale_factor,
            "company_id": company_id,
            "year": calibration_date.year,
            "user_id": user_id
        }
        db.execute("INSERT INTO calibrations (serial_number, calibration_date, unit, scale_factor, company_id, year, user_id) VALUES (:serial_number, :calibration_date, :unit, :scale_factor, :company_id, :year, :user_id)", calibration)
        db.commit()
        print(f"Imported calibration: {serial_number}")
    finally:
        db.close()

def main():
    folder_path = input("Enter folder path containing Excel files: ")
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith((".xlsx", ".xls")):
                file_path = os.path.join(root, file)
                import_excel(file_path)

if __name__ == "__main__":
    main()