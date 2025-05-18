import React from 'react';
import { AppBar, Toolbar, Typography, Button } from '@mui/material';
import { Link } from 'react-router-dom';

const Navbar = () => {
  return (
    <AppBar position="static">
      <Toolbar>
        <Typography variant="h6" sx={{ flexGrow: 1 }}>
          SSDL Calibration
        </Typography>
        <Button color="inherit" component={Link} to="/">
          Dashboard
        </Button>
        <Button color="inherit" component={Link} to="/new">
          New Calibration
        </Button>
        <Button color="inherit" component={Link} to="/search">
          Search
        </Button>
      </Toolbar>
    </AppBar>
  );
};

export default Navbar;