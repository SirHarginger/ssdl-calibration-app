import api from '../services/api';
import axios from 'axios';

jest.mock('axios');

test('fetches calibrations', async () => {
  const data = [{ id: 1, serial_number: 'TEST123' }];
  axios.get.mockResolvedValue({ data });
  const response = await api.get('/calibrations');
  expect(response.data).toEqual(data);
});