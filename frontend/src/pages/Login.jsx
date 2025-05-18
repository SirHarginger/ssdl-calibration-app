import React, { useState } from 'react';
import { Container, Typography, TextField, Button, Box } from '@mui/material';
import api from '../services/api';
import Navbar from '../components/Navbar';

const Login = () => {
  const [credentials, setCredentials] = useState({ username: '', password: '' });

  const handleChange = (e) => {
    setCredentials({ ...credentials, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await api.post('/auth/jwt/login', credentials);
      localStorage.setItem('token', response.data.access_token);
      // Redirect to dashboard
    } catch (error) {
      console.error('Login error:', error);
    }
  };

  return (
    <>
      <Navbar />
      <Container sx={{ mt: 4 }}>
        <Typography variant="h4" gutterBottom>
          Login
        </Typography>
        <Box component="form" onSubmit={handleSubmit} sx={{ maxWidth: 400 }}>
          <TextField
            label="Username"
            name="username"
            value={credentials.username}
            onChange={handleChange}
            fullWidth
            margin="normal"
          />
          <TextField
            label="Password"
            name="password"
            type="password"
            value={credentials.password}
            onChange={handleChange}
            fullWidth
            margin="normal"
          />
          <Button type="submit" variant="contained" color="primary" sx={{ mt: 2 }}>
            Login
          </Button>
        </Box>
      </Container>
    </>
  );
};

export default Login;