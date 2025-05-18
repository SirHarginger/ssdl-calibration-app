# SSDL Calibration Backend

FastAPI backend for the SSDL Calibration Web Application.

## Setup

1. Navigate to backend:
   ```powershell
   cd backend



Install dependencies:
powershell

poetry install

Copy environment file:
powershell

copy .env.example .env
# Edit .env with credentials

Run migrations:
powershell

poetry run alembic upgrade head

Start server:
powershell

poetry run uvicorn app.main:app --reload




