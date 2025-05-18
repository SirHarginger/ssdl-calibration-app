import pytest
from ...services.calculations import calculate_calibration_factor
from ...schemas.measurement import MeasurementCreate
from datetime import date

def test_calibration_factor():
    measurement = MeasurementCreate(
        calibration_id=1,
        ssd=1.0,
        measured_dose=100,
        measured_dose_unit="µSv/h",
        irradiation_time_min=None,
        background_measurements=[10, 10],
        source_on_measurements=[110, 110]
    )
    # Mock database session
    class MockDB:
        def query(self, model):
            class MockQuery:
                def filter(self, condition):
                    return self
                def first(self):
                    return MockCalibration()
            return MockQuery()
    
    class MockCalibration:
        calibration_date = date(2025, 5, 17)
        unit = "µSv/h"
        scale_factor = 1.0
    
    db = MockDB()
    result = calculate_calibration_factor(measurement, db)
    assert abs(result["calibration_factor"] - 14.723) < 0.1  # Approximate due to decay