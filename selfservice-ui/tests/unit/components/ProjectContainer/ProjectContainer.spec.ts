import { shallowMount, createLocalVue } from '@vue/test-utils';
import ProjectContainer from '@/components/ProjectContainer/ProjectContainer.vue';
import vuetify from 'vuetify';
import Vuex from 'vuex';
import { singleProject } from '../../mocks/projectinfo';
import VueRouter from 'vue-router';

describe('ProjectContainer.vue', () => {
  let wrapper: any;
  beforeEach(() => {
    const localVue = createLocalVue();
    localVue.use(vuetify);
    localVue.use(VueRouter);
    const router = new VueRouter();
    const store = new Vuex.Store({
      modules: {
        ProjectInfoModule: {
          namespaced: true,
          state: {},
          getters: {
            getSingleProjectInfo: jest.fn(() => {
              return { singleProject };
            }),
            getFinalProjectSubmissionStatus: jest.fn(),
            errorStatus: jest.fn(),
          },
          actions: {
            loadSingleProjectInfo: jest.fn(),
          },
        },
      },
    });

    wrapper = shallowMount(ProjectContainer, {
      localVue,
      store,
      router,
      mocks: { $t: jest.fn(() => {}) }, // tslint:disable-line
    });
  });

  it('renders props when passed', () => {
    expect(wrapper.element).toMatchSnapshot();
  });
});
