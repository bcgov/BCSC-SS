import { shallowMount, mount } from '@vue/test-utils';
import TeamSummary from '@/components/CreateApp/TeamSummary.vue';
import Vuetify from 'vuetify';
import Vuex from 'vuex';
let vuetify: any;
vuetify = new Vuetify();

describe('TeamSummary.vue', () => {
  const store = new Vuex.Store({
    modules: {
      TeamRolesModule: {
        namespaced: true,
        state: {},
        getters: {
          getTeamList: jest.fn(() => {
            return {
              team: [
                {
                  email: 'e@e.com',
                  firstName: 'fname',
                  id: 1,
                  lastName: 'lname',
                  phone: '09870987654321',
                  role: 2
                },
                {
                  email: 'bb@test.com',
                  firstName: 'john',
                  id: 17,
                  lastName: 'bb',
                  phone: '987654321',
                  role: 3
                },
                {
                  email: 'user@yopmail.com',
                  firstName: 'John',
                  id: 1,
                  lastName: 'Doe',
                  phone: '',
                  role: 1
                }
              ]
            };
          })
        },
        actions: {
          loadTeam: jest.fn()
        }
      },
      SharedModule: {
        namespaced: true,
        state: {},
        getters: {
          isRedirectFromSummaryPage: jest.fn()
        },
        actions: {
          redirectFromSummaryPage: jest.fn()
        }
      }
    }
  });

  const mountFunction = (options: any) => {
    return mount(TeamSummary, {
      store,
      vuetify,
      mocks: { $t: jest.fn(() => { }) }, // tslint:disable-line
      ...options
    });
  };

  it('renders props when passed with gettors', () => {
    const teamSummary = mountFunction({});

    expect(teamSummary.element).toMatchSnapshot();
  });

  it('render data', () => {
    const projectSummary = mountFunction({});
    projectSummary.setData({ isLoading: false });
    expect(projectSummary.element).toMatchSnapshot();
  });
});

describe('TeamSummary.vue', () => {
  it('renders props when passed', () => {
    const store = new Vuex.Store({
      modules: {
        TeamRolesModule: {
          namespaced: true,
          state: {},
          getters: {
            getTeamList: jest.fn()
          },
          actions: {
            loadTeam: jest.fn()
          }
        },
        SharedModule: {
          namespaced: true,
          state: {},
          getters: {
            isRedirectFromSummaryPage: jest.fn()
          },
          actions: {
            redirectFromSummaryPage: jest.fn()
          }
        }
      }
    });
    const teamSummary = shallowMount(TeamSummary, {
      vuetify,
      store,
      mocks: { $t: jest.fn(() => { }) } // tslint:disable-line
    });

    expect(teamSummary.element).toMatchSnapshot();
  });
});
