import React, { useState } from 'react';
import { Container, Typography, Button } from '@mui/material';
import CalibrationForm from '../components/CalibrationForm';
import ResultsTable from '../components/ResultsTable';
import api from '../services/api';
import Navbar from '../components/Navbar';

const NewCalibration = () => {
  const [calibrationId, setCalibrationId] = useState(null);
  const [results, setResults] = useState(null);

  const handleCalibrationCreated = (calibration) => {
    setCalibrationId(calibration.id);
    // Add measurement form or redirect to add measurements
  };

  const handleCalculate = async () => {
    if (!calibrationId) return;
    try {
      const response = await api.post(`/calculate/${calibrationId}`);
      setResults(response.data);
    } catch (error) {
      console.error('Error calculating:', error);
    }
  };

  const handleExport = async () => {
    if (!calibrationId) return;
    try {
      const response = await api.get(`/export/${calibrationId}`, { responseType: 'blob' });
      const url = window.URL.createObjectURL(new Blob([response.data]));
      const link = document.createElement('a');
      link.href = url;
      link.setAttribute('download', `certificate_${calibrationId}.docx`);
      document.body.appendChild(link);
      link.click();
    } catch (error) {
      console.error('Error exporting certificate:', error);
    }
  };

  return (
    <>
      <Navbar />
      <Container sx={{ mt: 4 }}>
        <Typography variant="h4" gutterBottom>
          New Calibration
        </Typography>
        {!calibrationId && <CalibrationForm onSubmit={handleCalibrationCreated} />}
        {calibrationId && (
          <>
            <Button variant="contained" onClick={handleCalculate} sx={{ m: 2 }}>
              Calculate
            </Button>
            <Button variant="contained" onClick={handleExport} sx={{ m: 2 }}>
              Export Certificate
            </Button>
            {results && <ResultsTable results={results.results} summary={results} />}
          </>
        )}
      </Container>
    </>
  );
};

export default NewCalibration;