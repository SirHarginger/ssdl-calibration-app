from fastapi.testclient import TestClient
from ...main import app

client = TestClient(app)

def test_create_calibration():
    response = client.post("/api/calibrations/", json={
        "serial_number": "TEST123",
        "calibration_date": "2025-05-17",
        "unit": "µSv/h",
        "scale_factor": 1.0,
        "company_id": 1
    })
    assert response.status_code == 401  # Requires authentication