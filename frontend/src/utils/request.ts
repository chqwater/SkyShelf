import axios, { AxiosInstance, AxiosError, AxiosResponse, InternalAxiosRequestConfig } from 'axios';
import { ElMessage } from 'element-plus';

const service: AxiosInstance = axios.create({
    baseURL: '',
    timeout: 5000
});

service.interceptors.request.use((config: any) => {
    config.headers['Content-Type'] = 'application/json';
    return config
  })

  service.interceptors.response.use(response => {
    const res = response.data
  
    if (res.code !== 200) {
      ElMessage({
        message: res.message || 'Error occurred',
        type: 'error',
        duration: 50000
      })
      return Promise.reject(new Error(res.message || 'Error occurred'))
    } else {
      return res
    }
  }, error => {
    console.error('Request error', error)
    ElMessage({
      message: error.message || 'Network error',
      type: 'error',
      duration: 5000
    })
    return Promise.reject(error)
  })

export default service;
