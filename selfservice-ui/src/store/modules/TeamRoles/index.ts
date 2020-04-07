import { Module } from 'vuex';
import { getters } from './getters';
import { actions } from './actions';
import { mutations } from './mutations';
import { TeamRoleState } from './types';
import { RootState } from '../../types';

/**
 * Sharedmodule state
 */
export const state: TeamRoleState = {
  teamRoles: {},
  isLoading: false,
  successStatus: false,
  errorStatus: false
};

const namespaced: boolean = true;

const SharedModule: Module<TeamRoleState, RootState> = {
  namespaced,
  state,
  getters,
  actions,
  mutations
};

export default SharedModule;
