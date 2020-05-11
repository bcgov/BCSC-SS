import { Module } from 'vuex';
import { getters } from './getters';
import { actions } from './actions';
import { mutations } from './mutations';
import { TestAccountState } from './types';
import { RootState } from '../../types';

/**
 * Sharedmodule state
 */
export const state: TestAccountState = {
  testAccounts: {},
  isLoading: false,
  successStatus: false,
  errorStatus: false,
  testAccountCount: {},
};

const namespaced: boolean = true;

const SharedModule: Module<TestAccountState, RootState> = {
  namespaced,
  state,
  getters,
  actions,
  mutations,
};

export default SharedModule;
