import { Module } from 'vuex';
import { getters } from './getters';
import { actions } from './actions';
import { mutations } from './mutations';
import { SharedState } from './types';
import { RootState } from '../../types';

/**
 * projectinfo state
 */
export const state: SharedState = {
  isSummaryPage: true
};

const namespaced: boolean = true;

const ProjectInfoModule: Module<SharedState, RootState> = {
  namespaced,
  state,
  getters,
  actions,
  mutations
};

export default ProjectInfoModule;
