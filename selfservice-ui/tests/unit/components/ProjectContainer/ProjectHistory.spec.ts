import { shallowMount, createLocalVue } from '@vue/test-utils';
import ProjectHistory from '@/components/ProjectContainer/ProjectHistory.vue';
import vuetify from 'vuetify';
import Vuex from 'vuex';
import { singleProject } from '../../mocks/projectinfo';

describe('ProjectHistory.vue', () => {
  let wrapper: any;
  beforeEach(() => {
    const localVue = createLocalVue();
    localVue.use(vuetify);
    const store = new Vuex.Store({
      modules: {
        ProjectInfoModule: {
          namespaced: true,
          state: {},
          getters: {
            getProjectHistory: jest.fn(() => {
              return { singleProject };
            }),
          },
          actions: {
            loadProjectHistory: jest.fn(),
          },
        },
      },
    });

    wrapper = shallowMount(ProjectHistory, {
      localVue,
      store,
      mocks: { $t: jest.fn(() => {}) }, // tslint:disable-line
    });
  });

  it('renders props when passed', () => {
    expect(wrapper.element).toMatchSnapshot();
  });
});
