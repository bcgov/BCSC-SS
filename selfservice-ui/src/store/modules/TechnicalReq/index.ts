import { Module } from 'vuex';
import { getters } from './getters';
import { actions } from './actions';
import { mutations } from './mutations';
import { TechnicalReqState } from './types';
import { RootState } from '../../types';
import { TechnicalReqModel } from '@/models/TechnicalReqModel';

/**
 * technicalreq state
 */
export const state: TechnicalReqState = {
  loading: false,
  successStatus: false,
  errorStatus: false,
  singleTechnicalReq: {
    projectId: '',
    clientUri: '',
    redirectUris: [],
    jwksUri: '',
    idTokenSignedResponseAlg: '',
    userinfoSignedResponseAlg: ''
  },
  message: ''
};

const namespaced: boolean = true;

const TechnicalReqModule: Module<TechnicalReqState, RootState> = {
  namespaced,
  state,
  getters,
  actions,
  mutations
};

export default TechnicalReqModule;
