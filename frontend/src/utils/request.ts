import axios, { AxiosInstance, AxiosError, AxiosResponse, InternalAxiosRequestConfig } from 'axios';
import { ElMessage } from 'element-plus';

const service: AxiosInstance = axios.create({
    baseURL: 'http://127.0.0.1:8000',
    timeout: 5000
});

service.interceptors.request.use((config: any) => {
    config.headers['Content-Type'] = 'application/json';
    return config
  })

  service.interceptors.response.use(response => {
    const res = response.data;
    console.log(res)
    const status = response.status;
    console.log(status)
    if (status !== 200) {
      return Promise.reject(new Error(res.detail || 'Error occurred'));
    } else {
      return res; 
    }
  }, error => {
    console.error('Request error', error);
    return Promise.reject(error);
  })

export default service;
