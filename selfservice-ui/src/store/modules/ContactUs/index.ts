import { Module } from 'vuex';
import { getters } from './getters';
import { actions } from './actions';
import { mutations } from './mutations';
import { TestAccountState } from './types';
import { RootState } from '../../types';
import { contactDetailsSample } from './defaults';

/**
 * Sharedmodule state
 */
export const state: TestAccountState = {
  contactDetails: contactDetailsSample(),
  isLoading: false,
  successStatus: false,
  errorStatus: false,
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
