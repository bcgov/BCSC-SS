import { MutationTree } from 'vuex';
import { KeyCloakState } from './types';

/**
 * mutation
 */
export const mutations: MutationTree<KeyCloakState> = {
  /**
   * set loading
   * @param {*} state
   * @param {*} flag
   */

  SET_LOADING(state, flag: any) {
    state.loading = flag;
  },
  /**
   * setting login state
   * @param {*} state
   * @param {bool} authenticated
   */
  SET_LOGIN(state, authenticated: boolean) {
    state.authenticated = authenticated;
  },
  /**
   * setting keyauth
   *
   * @param {*} state
   * @param {*} keycloak
   */
  SET_KEY_AUTH(state, keycloak: any) {
    state.keycloakAuth = keycloak;
  },

  /**
   * setting token
   *
   * @param {*} state
   * @param {string} token
   */
  SET_TOKEN(state, token: string) {
    state.token = token;
  },

  /**
   * setting logout
   *
   * @param {*} state
   * @param {boolean} authenticated
   */
  SET_LOGOUT(state, authenticated: boolean) {
    state.authenticated = authenticated || false;
    state.keycloakAuth = {};
    state.token = '';
  },
  SET_USER_PROFILE(state, profile: any) {
    state.profile = profile;
  },

  SET_USER_ROLES(state, { isAdmin, isClient }) {
    state.isAdmin = isAdmin;
    state.isClient = isClient;
  }
};
