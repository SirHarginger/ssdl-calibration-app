from whoosh.index import create_in, open_dir
from whoosh.fields import Schema, TEXT, ID, NUMERIC, DATETIME
from whoosh.qparser import MultifieldParser
from sqlalchemy.orm import Session
from ...models.calibration import Calibration
from ...models.company import Company
import os

INDEX_DIR = os.getenv("WHOOSH_INDEX_PATH", "search_index/index")
schema = Schema(
    calibration_id=ID(stored=True),
    serial_number=TEXT,
    company_name=TEXT,
    year=NUMERIC,
    calibration_date=DATETIME,
    unit=TEXT
)

if not os.path.exists(INDEX_DIR):
    os.makedirs(INDEX_DIR)
    create_in(INDEX_DIR, schema)

def update_index(calibration: Calibration, db: Session):
    ix = open_dir(INDEX_DIR)
    writer = ix.writer()
    company = db.query(Company).filter(Company.id == calibration.company_id).first()
    writer.add_document(
        calibration_id=str(calibration.id),
        serial_number=calibration.serial_number,
        company_name=company.name if company else "",
        year=calibration.year,
        calibration_date=calibration.calibration_date,
        unit=calibration.unit
    )
    writer.commit()

def search_calibrations(query_str: str, year: int = None, company: str = None, unit: str = None, db: Session = None):
    ix = open_dir(INDEX_DIR)
    with ix.searcher() as searcher:
        query = MultifieldParser(["serial_number", "company_name", "unit"], schema=schema).parse(query_str)
        results = searcher.search(query, limit=20)
        calibration_ids = [int(hit["calibration_id"]) for hit in results]
        calibrations = db.query(Calibration).filter(Calibration.id.in_(calibration_ids)).all()
        return [calibration.__dict__ for calibration in calibrations]