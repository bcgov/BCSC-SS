export const BASE_URL =
  process.env.VUE_APP_API_BASE_URL || 'http://localhost:3000/';
export const LOCAL_BASE_URL = 'http://localhost:3000/';
export const PROJECTINFO_URL = BASE_URL + 'project/info';
export const TECHNICALREQ_URL = BASE_URL + 'project/<projectId>/technical-req';
export const USER_URL = BASE_URL + 'user';
export const PACKAGE_URL = BASE_URL + 'scope-package';
export const OIDCCONFIG_URL = BASE_URL + 'project/<projectId>/oidc-config';
