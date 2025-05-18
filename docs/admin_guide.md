# SSDL Calibration Web Application Admin Guide

## Overview
This guide is for administrators managing the SSDL Calibration Web Application.

## User Management
1. **Access**: Login as an admin (role: 'admin').
2. **Add User**:
   - Via API: POST `/users` with username, email, password, role ('tech' or 'admin').
   - Example: `curl -X POST http://localhost:8000/users -d '{"username":"newuser","email":"user@lab.com","password":"securepass","role":"tech"}'`.
3. **Remove User**: Contact DevOps to disable accounts (not implemented in UI).

## Data Management
1. **Import Historical Data**:
   - Upload Excel files via POST `/api/import` (requires folder structure: Year → Company → Instrument).
   - Check logs for errors (backend/logs).
2. **Backup Database**:
   - Run `docker exec <postgres-container> pg_dump -U ssdl_user ssdl_db > backup.sql`.
3. **Restore Database**: Consult DevOps for restoration.

## Deployment
- **Local**: Run `docker-compose up`.
- **Production**: Deploy on AWS/lab server (see DevOps).
- **CI/CD**: Managed via GitHub Actions.

## Troubleshooting
- **Backend Errors**: Check logs in `backend/logs`.
- **Frontend Issues**: Use browser DevTools (F12).
- **Contact**: DevOps team for support.

## Notes
- Ensure `template.docx` is provided for certificates.
- Validate Excel imports with sample files.