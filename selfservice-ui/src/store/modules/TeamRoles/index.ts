import { Module } from 'vuex';
import { getters } from './getters';
import { actions } from './actions';
import { mutations } from './mutations';
import { TeamRoleState } from './types';
import { RootState } from '../../types';
import { memberDetails } from './defaults';

/**
 * Sharedmodule state
 */
export const state: TeamRoleState = {
  teamRoles: [],
  isLoading: false,
  successStatus: false,
  errorStatus: false,
  memberAdded: false,
  memberAddedError: false,
  memberAddedErrorList: {},
  memberDetails
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
