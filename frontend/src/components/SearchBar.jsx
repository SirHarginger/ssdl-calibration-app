import React, { useState } from 'react';
import { TextField, Button, Box } from '@mui/material';
import api from '../services/api';

const SearchBar = ({ onSearch }) => {
  const [query, setQuery] = useState('');

  const handleSearch = async () => {
    try {
      const response = await api.get('/search', { params: { query } });
      onSearch(response.data.results);
    } catch (error) {
      console.error('Error searching:', error);
    }
  };

  return (
    <Box sx={{ display: 'flex', gap: 2, p: 2 }}>
      <TextField
        label="Search Calibrations"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        fullWidth
      />
      <Button variant="contained" onClick={handleSearch}>
        Search
      </Button>
    </Box>
  );
};

export default SearchBar;