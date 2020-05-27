import { shallowMount } from '@vue/test-utils';
import Dashboard from '@/components/Dashboard/Dashboard.vue';
import Vuetify from 'vuetify';
import Vuex from 'vuex';
let vuetify: any;
vuetify = new Vuetify();

describe('Dashboard.vue', () => {
  const store = new Vuex.Store({
    modules: {
      ProjectInfoModule: {
        namespaced: true,
        state: {},
        getters: {
          getProjectInfoList: jest.fn(() => {
            return [];
          }),
        },
        actions: {
          loadProjectInfo: jest.fn(),
        },
      },
      KeyCloakModule: {
        namespaced: true,
        state: {},
        getters: {
          userProfile: jest.fn(() => {
            return {
              firstName: 'user',
              lastName: 'lastName',
            };
          }),
          isLoggedin: jest.fn(() => {
            return true;
          }),
          isAdmin: jest.fn(() => {
            return true;
          }),
        },
        actions: { setLogout: jest.fn() },
      },
    },
  });

  const mountFunction = (options: any) => {
    return shallowMount(Dashboard, {
      store,
      vuetify,
      mocks: { $t: jest.fn(() => {}) }, // tslint:disable-line
      ...options,
    });
  };

  it('renders props when passed with gettors', () => {
    const dashboard = mountFunction({});
    expect(dashboard.element).toMatchSnapshot();
  });
});
