import { Module } from 'vuex';
import { getters } from './getters';
import { actions } from './actions';
import { mutations } from './mutations';
import { ProjectInfoState } from './types';
import { RootState } from '../../types';

/**
 * projectinfo state
 */
export const state: ProjectInfoState = {
  projectinfoList: [],
  loading: false,
  successStatus: false,
  errorStatus: false,
  singleProjectInfo: {
    organizationName: '',
    projectName: '',
    myRole: '',
    description: ''
  },
  message: ''
};

const namespaced: boolean = true;

const ProjectInfoModule: Module<ProjectInfoState, RootState> = {
  namespaced,
  state,
  getters,
  actions,
  mutations
};

export default ProjectInfoModule;
