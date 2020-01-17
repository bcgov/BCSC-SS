import { ActionTree } from 'vuex';
import { KeyCloakState } from './types';
import { RootState } from '../../types';
import KeycloakService from '@/services/keycloakservice';
import { UserService } from '@/services/userService';
// import axios from '@/lib/axios';
import router from '@/router';
// import { USER_URL } from '@/config/urlList';
// import { UserService } from '@/services/userService';

/**
 * Keycloak Actions
 *
 */
export const actions: ActionTree<KeyCloakState, RootState> = {
  setLogin({ commit }: any, login: any) {
    commit('SET_LOGIN', login);
  },

  /**
   * setKeyCloakAuth when token provide
   * @param {*} { commit }
   * @param {*} keycloak
   */
  async setKeyCloakAuth(state: any, data) {
    const { commit, dispatch } = state;
    const { keycloak, path, next } = data;
    const token = keycloak.token || false;
    if (token) {
      commit('SET_LOGIN', true);
      commit('SET_KEY_AUTH', keycloak);
      commit('SET_TOKEN');
      sessionStorage.setItem('keycloak_token', token);
      try {
        const user = await UserService.createUser();
        dispatch('setUserProfile', user.data);
        dispatch('userRedirect', { path, next });
        // if (user.data && user.data.firstTimeLogin) {
        //   router.push({ path: '/profile' });
        // } else {
        //   dispatch('userRedirect', path);
        // }
      } catch {
        dispatch('userRedirect', { path, next });
      }
    }
  },

  /**
   * setLogout remove token when user logout
   * @param {*} { commit }
   */
  setLogout({ commit }: any) {
    commit('SET_LOGOUT', false);
    sessionStorage.removeItem('keycloak_token');
    KeycloakService.logout();
  },
  /**
   * setUserProfile
   * @param {*} { commit }
   * @param {*} keycloak
   */
  setUserProfile({ commit }: any, profile: any) {
    commit('SET_USER_PROFILE', profile);
  },
  /**
   * setKeyCloakAuth when token provide
   * @param {*} { commit }
   * @param {*} keycloak
   */
  setUserRole({ commit }: any, userRole: string[]) {
    let isAdmin = false;
    let isClient = false;

    if (userRole && userRole.length > 0) {
      const isadminRole = userRole.indexOf('ss_admin');
      if (isadminRole !== -1) {
        isAdmin = true;
      } else {
        const isClientRole = userRole.indexOf('ss_client');
        if (isClientRole !== -1) {
          isClient = true;
        }
      }
    }
    commit('SET_USER_ROLES', { isAdmin, isClient });
    commit('SET_TOKEN');
  },

  /**
   * setAuth when token provide
   * @param {*} { commit }
   * @param {*} keycloak
   */
  userRedirect(store: any, { path, next }) {
    if (path === '/login') {
      if (store.state.isClient || store.state.isAdmin) {
        router.push({ path: '/project' });
      }
    } else {
      next();
    }
  }
};
