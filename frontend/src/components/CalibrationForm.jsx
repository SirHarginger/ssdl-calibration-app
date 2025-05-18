import React, { useState } from 'react';
import { TextField, Button, Select, MenuItem, FormControl, InputLabel, Box } from '@mui/material';
import api from '../services/api';

const CalibrationForm = ({ onSubmit }) => {
  const [formData, setFormData] = useState({
    serial_number: '',
    calibration_date: '',
    unit: 'µSv/h',
    scale_factor: 1.0,
    initial_temperature: '',
    initial_pressure: '',
    initial_humidity: '',
    final_temperature: '',
    final_pressure: '',
    final_humidity: '',
    company_id: 1
  });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await api.post('/calibrations', formData);
      onSubmit(response.data);
    } catch (error) {
      console.error('Error creating calibration:', error);
    }
  };

  return (
    <Box component="form" onSubmit={handleSubmit} sx={{ p: 2 }}>
      <TextField
        label="Serial Number"
        name="serial_number"
        value={formData.serial_number}
        onChange={handleChange}
        fullWidth
        margin="normal"
      />
      <TextField
        label="Calibration Date"
        name="calibration_date"
        type="date"
        value={formData.calibration_date}
        onChange={handleChange}
        fullWidth
        margin="normal"
        InputLabelProps={{ shrink: true }}
      />
      <FormControl fullWidth margin="normal">
        <InputLabel>Unit</InputLabel>
        <Select name="unit" value={formData.unit} onChange={handleChange}>
          <MenuItem value="C/s">C/s</MenuItem>
          <MenuItem value="µSv/h">µSv/h</MenuItem>
          <MenuItem value="mrem/h">mrem/h</MenuItem>
          <MenuItem value="accumulated_dose">Accumulated Dose</MenuItem>
        </Select>
      </FormControl>
      <TextField
        label="Scale Factor"
        name="scale_factor"
        type="number"
        value={formData.scale_factor}
        onChange={handleChange}
        fullWidth
        margin="normal"
      />
      <TextField
        label="Initial Temperature (°C)"
        name="initial_temperature"
        type="number"
        value={formData.initial_temperature}
        onChange={handleChange}
        fullWidth
        margin="normal"
      />
      <TextField
        label="Initial Pressure (kPa)"
        name="initial_pressure"
        type="number"
        value={formData.initial_pressure}
        onChange={handleChange}
        fullWidth
        margin="normal"
      />
      <TextField
        label="Initial Humidity (%)"
        name="initial_humidity"
        type="number"
        value={formData.initial_humidity}
        onChange={handleChange}
        fullWidth
        margin="normal"
      />
      <TextField
        label="Final Temperature (°C)"
        name="final_temperature"
        type="number"
        value={formData.final_temperature}
        onChange={handleChange}
        fullWidth
        margin="normal"
      />
      <TextField
        label="Final Pressure (kPa)"
        name="final_pressure"
        type="number"
        value={formData.final_pressure}
        onChange={handleChange}
        fullWidth
        margin="normal"
      />
      <TextField
        label="Final Humidity (%)"
        name="final_humidity"
        type="number"
        value={formData.final_humidity}
        onChange={handleChange}
        fullWidth
        margin="normal"
      />
      <TextField
        label="Company ID"
        name="company_id"
        type="number"
        value={formData.company_id}
        onChange={handleChange}
        fullWidth
        margin="normal"
      />
      <Button type="submit" variant="contained" color="primary" sx={{ mt: 2 }}>
        Create Calibration
      </Button>
    </Box>
  );
};

export default CalibrationForm;