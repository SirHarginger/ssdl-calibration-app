import pytest
from ...services.import_data import import_excel
from fastapi import UploadFile
from io import BytesIO

def test_import_excel():
    # Placeholder test; requires actual Excel file structure
    file_content = b"Serial Number,Calibration Date\nTEST123,2025-05-17"
    file = UploadFile(filename="test.xlsx", file=BytesIO(file_content))
    
    class MockDB:
        def query(self, model):
            return self
        def filter(self, condition):
            return self
        def first(self):
            return None
        def add(self, obj):
            pass
        def commit(self):
            pass
        def refresh(self, obj):
            pass
    
    calibration = import_excel(file, MockDB(), 1)
    assert calibration.serial_number == "TEST123"