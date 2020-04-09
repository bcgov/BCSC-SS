import { shallowMount } from '@vue/test-utils';
import TeamRoles from '@/components/TeamRoles/TeamRoles.vue';
import Vuetify from 'vuetify';
import Vuex from 'vuex';
let vuetify: any;
vuetify = new Vuetify();

describe('TeamRoles.vue', () => {
  const store = new Vuex.Store({
    modules: {
      TeamRolesModule: {
        namespaced: true,
        state: {},
        getters: {
          successStatus: jest.fn(),
          errorStatus: jest.fn(),
          isLoading: jest.fn(),

          getTeamList: jest.fn(() => {
            return [];
          })
        },
        actions: {
          loadTeam: jest.fn(),
          clearStatus: jest.fn()
        }
      }
    }
  });

  const mountFunction = (options: any) => {
    return shallowMount(TeamRoles, {
      store,
      vuetify,
      mocks: { $t: jest.fn(() => {}) }, // tslint:disable-line
      ...options
    });
  };

  it('renders props when passed with gettors', () => {
    const TeamRolesPage = mountFunction({});
    expect(TeamRolesPage.element).toMatchSnapshot();
  });
});
