import Keycloak from 'keycloak-js';
import store from '@/store';

const sslRequired = 'external';
const confidentialPort = 0;
/** key cloak settings */
/* tslint:disable */
const keycloakConfig: any = {
  realm: process.env.VUE_APP_KEYCLOAK_REALM,
  url: process.env.VUE_APP_KEYCLOAK_URL,
  'ssl-required': sslRequired,
  clientId: process.env.VUE_APP_KEYCLOAK_CLIENT,
  'confidential-port': confidentialPort,
};
/* tslint:enable */

/**
 * Keycloak service - SSO Login
 */
export default class KeycloakService {
  /**
   * Logins keycloak service
   */
  public static login() {
    KeycloakService.keycloak.login();
  }

  /**
   * Logouts keycloak service
   */
  public static logout() {
    KeycloakService.keycloak.logout({
      redirectUri: window.location.origin,
    });
  }

  /**
   * Determines whether authenticated
   * @returns  {bool}
   */
  public static isAuthenticated() {
    return KeycloakService.keycloak.authenticated;
  }

  /**
   * Tokens keycloak service
   * @returns  {string}
   */
  public static token() {
    return KeycloakService.keycloak.token;
  }

  /**
   * Updates token
   * @param time  - refresh time in sec
   * @returns  updated tocken
   */
  public static updateToken(time: number) {
    return KeycloakService.keycloak.updateToken(time);
  }

  public static getUserInfo() {
    // let token = KeycloakService.token();
    // if (!token) {
    const token = KeycloakService.decodeToken();
    // }
    // console.log('token', token);
    return {
      lastName: token.lastname,
      firstName: token.firstname,
      email: token.email,
      roles: token.realm_access.roles,
      keycloakGuid: token.jti,
      userName: token.username,
    };
  }
  public static userRoles(): [] {
    const token = KeycloakService.decodeToken();
    return token.realm_access.roles || ['user'];
  }
  public static decodeToken() {
    try {
      const token: string = sessionStorage.getItem('keycloak_token') || '';
      const base64Url = token && token.split('.')[1];
      const base64 = decodeURIComponent(
        window
          .atob(base64Url)
          .split('')
          .map((c) => {
            return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
          })
          .join('')
      );
      return JSON.parse(base64);
    } catch (error) {
      throw new Error('Error parsing JWT - ' + error);
    }
  }

  /**
   * Keycloakfulls keycloak service
   * @returns full keyclock service Object
   */
  public static keycloakfull() {
    return KeycloakService.keycloak;
  }

  public static init(
    next: any,
    silentCheckSsoRedirectUri: string,
    roles: [],
    fromUrl: string = ''
  ) {
    const storeState = store.state;
    const isLoggedin = storeState.KeyCloakModule.authenticated;
    if (isLoggedin) {
      next();
    } else {
      KeycloakService.keycloak
        .init({
          onLoad: 'login-required',
          redirectUri: window.location.origin + silentCheckSsoRedirectUri,
        })
        .success(() => {
          store.dispatch('KeyCloakModule/setKeyCloakAuth', {
            keycloak: KeycloakService.keycloak,
            path: silentCheckSsoRedirectUri,
            next,
            fromUrl,
          });

          store.dispatch(
            'KeyCloakModule/setUserRole',
            KeycloakService.userRoles()
          );
          setInterval(() => {
            KeycloakService.keycloak
              .updateToken(5)
              .success((refreshed: any) => {
                if (refreshed) {
                  // console.log('token refreshed', refreshed);
                  store.dispatch('KeyCloakModule/setKeyCloakAuth', {
                    keycloak: KeycloakService.keycloak,
                  });
                }
              })
              .error(() => {
                store.dispatch(
                  'KeyCloakModule/setLogout',
                  KeycloakService.keycloak
                );
                // console.info('Failed to refresh token');
              });
          }, 6000);
          if (KeycloakService.checkPermission(roles)) {
            next();
          } else {
            next({ name: 'Unauthorized' });
          }
        })
        .error(() => {
          /* tslint:disable */
          console.log('keycloak init is not working. check  configuration ');
          /* tslint:enable */
          // console.info('Failed to refresh token');
        });
      next();
    }
  }

  public static checkPermission(roles: [] = []) {
    const userRolesAvailable = KeycloakService.userRoles();
    let hasAccess = false;
    if (KeycloakService.isAuthenticated()) {
      if (roles && roles.length > 0) {
        roles.forEach((role) => {
          if (userRolesAvailable.indexOf(role) !== -1) {
            hasAccess = true;
          }
        });
        return hasAccess;
      } else {
        // if no roles provided, have access
        hasAccess = true;
      }
    }
    return hasAccess;
  }

  private static keycloak = Keycloak(keycloakConfig);
}
