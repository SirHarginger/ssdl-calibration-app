from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api import calibrations, measurements, calculations, upload, search, export
from fastapi_users import FastAPIUsers
from .database.db import engine, Base
from .models.user import User
from .utils.auth import auth_backend, user_manager

app = FastAPI(title="SSDL Calibration Web Application")

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create database tables
Base.metadata.create_all(bind=engine)

# Include API routers
app.include_router(calibrations.router, prefix="/api")
app.include_router(measurements.router, prefix="/api")
app.include_router(calculations.router, prefix="/api")
app.include_router(upload.router, prefix="/api")
app.include_router(search.router, prefix="/api")
app.include_router(export.router, prefix="/api")

# FastAPI Users for authentication
fastapi_users = FastAPIUsers[User, int](user_manager, [auth_backend])
app.include_router(
    fastapi_users.get_auth_router(auth_backend), prefix="/auth", tags=["auth"]
)
app.include_router(
    fastapi_users.get_users_router(), prefix="/users", tags=["users"]
)

@app.get("/")
def read_root():
    return {"message": "SSDL Calibration Web Application"}