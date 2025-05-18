import React, { useEffect, useState } from 'react';
import { Container, Typography } from '@mui/material';
import { useParams } from 'react-router-dom';
import api from '../services/api';
import ResultsTable from '../components/ResultsTable';
import Navbar from '../components/Navbar';

const Results = () => {
  const { id } = useParams();
  const [results, setResults] = useState(null);

  useEffect(() => {
    const fetchResults = async () => {
      try {
        const response = await api.post(`/calculate/${id}`);
        setResults(response.data);
      } catch (error) {
        console.error('Error fetching results:', error);
      }
    };
    fetchResults();
  }, [id]);

  return (
    <>
      <Navbar />
      <Container sx={{ mt: 4 }}>
        <Typography variant="h4" gutterBottom>
          Calibration Results
        </Typography>
        {results ? (
          <ResultsTable results={results.results} summary={results} />
        ) : (
          <Typography>Loading...</Typography>
        )}
      </Container>
    </>
  );
};

export default Results;