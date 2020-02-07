import { mount, createLocalVue } from '@vue/test-utils';
import ProjectSummary from '@/components/CreateApp/ProjectSummary.vue';
import Vuetify from 'vuetify';
import Vuex from 'vuex';

describe('ProjectSummary.vue', () => {
  let vuetify: any;
  const localVue = createLocalVue();

  const $t = localVue.use(Vuetify);
  localVue.use(Vuex);
  vuetify = new Vuetify();
  const store = new Vuex.Store({
    modules: {
      PackageAndTestModule: {
        namespaced: true,
        state: {},
        getters: {
          isLoggedin: jest.fn(),
          successStatus: jest.fn(),
          errorStatus: jest.fn()
        },
        actions: {
          addProjectSummaryToProject: jest.fn()
        }
      }
    }
  });

  const mountFunction = (options: any) => {
    return mount(ProjectSummary, {
      store,
      vuetify,
      localVue,
      mocks: { $t: jest.fn(() => {}) }, // tslint:disable-line
      ...options
    });
  };

  it('renders props when passed', () => {
    const TestReqWrapper = mountFunction({});

    expect(TestReqWrapper.element).toMatchSnapshot();
  });
});
