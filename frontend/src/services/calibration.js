import api from './api';

export const createCalibration = (data) => api.post('/calibrations', data);
export const getCalibration = (id) => api.get(`/calibrations/${id}`);
export const calculateCalibration = (id) => api.post(`/calculate/${id}`);
export const exportCertificate = (id) => api.get(`/export/${id}`, { responseType: 'blob' });