import { shallowMount } from '@vue/test-utils';
import ProjectInfoSummary from '@/components/CreateApp/ProjectInfoSummary.vue';
import Vuetify from 'vuetify';
import Vuex from 'vuex';

import { singleProject } from '../../mocks/projectinfo';

let vuetify: any;
vuetify = new Vuetify();

describe('ProjectInfoSummary.vue', () => {
  const storeData = new Vuex.Store({
    modules: {
      ProjectInfoModule: {
        namespaced: true,
        state: {},
        getters: {
          getSingleProjectInfo: jest.fn(() => {
            return {
              singleProject
            };
          }),
          getFinalProjectSubmissionStatus: jest.fn(),
          errorStatus: jest.fn()
        },
        actions: {
          loadSingleProjectInfo: jest.fn()
        }
      }
    }
  });

  const mountFunction = (options: any) => {
    return shallowMount(ProjectInfoSummary, {
      store: storeData,
      vuetify,
      mocks: { $t: jest.fn(() => {}) }, // tslint:disable-line
      ...options
    });
  };

  it('renders props when passed with gettors', () => {
    const projectInfoSummary = mountFunction({});

    expect(projectInfoSummary.element).toMatchSnapshot();
  });
});
