import React from 'react';
import { render, screen } from '@testing-library/react';
import CalibrationForm from '../components/CalibrationForm';

test('renders CalibrationForm', () => {
  render(<CalibrationForm onSubmit={() => {}} />);
  expect(screen.getByLabelText(/Serial Number/i)).toBeInTheDocument();
});