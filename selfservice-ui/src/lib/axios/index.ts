import axios from 'axios';
import router from '@/router';
import store from '@/store/index';

/** setting base header  */
const instance = axios.create();
instance.interceptors.request.use((config) => {
  config.headers.get['Content-Type'] = 'application/json';
  config.headers.post['Content-Type'] = 'application/json';
  config.headers.put['Content-Type'] = 'application/json';
  config.headers.patch['Content-Type'] = 'application/json';
  config.headers.delete['Content-Type'] = 'application/json';
  config.headers.common.Authorization = `Bearer ${sessionStorage.getItem(
    'keycloak_token'
  )}`;
  return config;
});

// Add a response interceptor
instance.interceptors.response.use(
  (response) => {
    return response;
  },
  async (error) => {
    // redirect unathorized request to unathorized page
    // resetprogress

    if (error.response.status === 401) {
      store.dispatch('ProjectInfoModule/resetprogress');
      await router.push('/unauthorized');
    }
    return Promise.reject(error);
  }
);

export default instance;
