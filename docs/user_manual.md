# SSDL Calibration Web Application User Manual

## Overview
This application helps Secondary Standard Dosimetry Lab staff manage equipment calibrations, replacing Excel templates.

## Getting Started
1. **Access the App**: Open http://localhost:3000 (or production URL).
2. **Login**: Use your credentials (contact admin for access).
3. **Dashboard**: View recent calibrations or search existing ones.

## Creating a Calibration
1. Navigate to **New Calibration**.
2. Enter:
   - Serial Number, Calibration Date, Unit (C/s, µSv/h, mrem/h, accumulated dose).
   - Scale Factor (default 1).
   - Environmental Conditions (temperature, pressure, humidity).
   - Company (select or search).
3. Add Measurements:
   - SSD (1.0m to 5.0m).
   - Measured Dose, Irradiation Time (for accumulated dose).
   - Background and Source-On measurements (multiple entries).
4. Click **Calculate** to view results.
5. Click **Export Certificate** to download the Word document.

## Searching Calibrations
1. Go to **Search**.
2. Enter query (e.g., "Company X 2023", serial number).
3. Filter by year, company, or unit.
4. View results and click to see details.

## Importing Historical Data
1. Contact admin to upload Excel files (Year → Company → Instrument structure).
2. Imported data appears in search results.

## Support
- **Admin Guide**: See `admin_guide.md`.
- **Contact**: Lab IT administrator for issues.