# Initialize PostgreSQL database
Write-Host "Setting up PostgreSQL database..."

# Start Docker Compose (ensure Docker Desktop is running)
docker-compose up -d db

# Wait for PostgreSQL to be ready
Start-Sleep -Seconds 10

# Run Alembic migrations
Set-Location ..\backend
poetry run alembic upgrade head

Write-Host "Database setup complete."