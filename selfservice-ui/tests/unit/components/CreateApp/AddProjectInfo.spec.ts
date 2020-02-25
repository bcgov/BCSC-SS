import { shallowMount } from '@vue/test-utils';
import AddProjectInfo from '@/components/CreateApp/AddProjectInfo.vue';
import Vuetify from 'vuetify';
import Vuex from 'vuex';

let vuetify: any;
vuetify = new Vuetify();

describe('AddProjectInfo.vue', () => {
  const store = new Vuex.Store({
    modules: {
      ProjectInfoModule: {
        namespaced: true,
        state: {},
        getters: {
          getSingleProjectInfo: jest.fn(),
          isLoggedin: jest.fn()
        },
        actions: {
          loadSingleProjectInfo: jest.fn()
        }
      },
      SharedModule: {
        namespaced: true,
        state: {},
        getters: {
          isRedirectFromSummaryPage: jest.fn()
        },
        actions: {
          rediectFromSummaryPage: jest.fn()
        }
      }
    }
  });

  const shallowMountFunction = (options: any) => {
    return shallowMount(AddProjectInfo, {
      vuetify,
      store,
      mocks: { $t: jest.fn(() => {}) }, // tslint:disable-line
      ...options
    });
  };

  it('renders props when passed', () => {
    const projectInfo = shallowMountFunction({});
    expect(projectInfo.element).toMatchSnapshot();
  });
  it('renders edit props when passed', () => {
    const projectInfo = shallowMountFunction({ propsData: { id: 1 } });
    expect(projectInfo.element).toMatchSnapshot();
  });
});
