import React, { useEffect, useState } from 'react';
import { Container, Typography } from '@mui/material';
import api from '../services/api';
import Navbar from '../components/Navbar';

const Dashboard = () => {
  const [calibrations, setCalibrations] = useState([]);

  useEffect(() => {
    const fetchCalibrations = async () => {
      try {
        const response = await api.get('/calibrations');
        setCalibrations(response.data);
      } catch (error) {
        console.error('Error fetching calibrations:', error);
      }
    };
    fetchCalibrations();
  }, []);

  return (
    <>
      <Navbar />
      <Container sx={{ mt: 4 }}>
        <Typography variant="h4" gutterBottom>
          Dashboard
        </Typography>
        <Typography>Recent Calibrations (Placeholder)</Typography>
        {/* Add table or list of calibrations */}
      </Container>
    </>
  );
};

export default Dashboard;