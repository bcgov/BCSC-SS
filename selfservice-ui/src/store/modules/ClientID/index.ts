import { Module } from 'vuex';
import { getters } from './getters';
import { actions } from './actions';
import { mutations } from './mutations';
import { ClientIdState } from './types';
import { RootState } from '../../types';

/**
 * ClientIdModule state
 */
export const state: ClientIdState = {
  apiData: [],
  loading: true,
  successStatus: false,
  errorStatus: false,
  message: ''
};

const namespaced: boolean = true;

const ClientIdModule: Module<ClientIdState, RootState> = {
  namespaced,
  state,
  getters,
  actions,
  mutations
};

export default ClientIdModule;
