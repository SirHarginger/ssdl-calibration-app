import React from 'react';
import { Table, TableBody, TableCell, TableHead, TableRow, Paper } from '@mui/material';

const ResultsTable = ({ results, summary }) => {
  return (
    <Paper sx={{ p: 2, mt: 2 }}>
      <Table>
        <TableHead>
          <TableRow>
            <TableCell>SSD (m)</TableCell>
            <TableCell>Ref Dose Rate (mSv/h)</TableCell>
            <TableCell>Corrected Dose</TableCell>
            <TableCell>Calibration Factor</TableCell>
            <TableCell>Avg Background</TableCell>
            <TableCell>Avg Source On</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {results.map((row, index) => (
            <TableRow key={index}>
              <TableCell>{row.ssd}</TableCell>
              <TableCell>{row.ref_dose_rate_msv_h.toFixed(4)}</TableCell>
              <TableCell>{row.corrected_dose.toFixed(2)}</TableCell>
              <TableCell>{row.calibration_factor.toFixed(4)}</TableCell>
              <TableCell>{row.avg_background.toFixed(2)}</TableCell>
              <TableCell>{row.avg_source_on.toFixed(2)}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
      <div>
        <p>Average Calibration Factor: {summary.average_calibration_factor.toFixed(4)}</p>
        <p>Standard Deviation: {summary.std_calibration_factor.toFixed(4)}</p>
      </div>
    </Paper>
  );
};

export default ResultsTable;