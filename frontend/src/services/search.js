import api from './api';

export const searchCalibrations = (query, params = {}) => api.get('/search', { params: { query, ...params } });