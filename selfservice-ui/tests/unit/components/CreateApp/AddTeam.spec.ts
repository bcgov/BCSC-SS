import { mount, createLocalVue } from '@vue/test-utils';
import AddTeam from '@/components/CreateApp/AddTeam.vue';
import Vuetify from 'vuetify';
import Vuex from 'vuex';
let vuetify: any;
vuetify = new Vuetify();

describe('AddTeam.vue', () => {
  let wrapper: any;
  const localVue = createLocalVue();

  localVue.use(Vuetify);
  localVue.use(Vuex);
  vuetify = new Vuetify();
  const store = new Vuex.Store({
    modules: {
      SharedModule: {
        namespaced: true,
        state: {},
        getters: {
          isRedirectFromSummaryPage: jest.fn()
        },
        actions: {
          redirectFromSummaryPage: jest.fn()
        }
      },
      TeamRolesModule: {
        namespaced: true,
        state: {},
        getters: {
          getTeamList: jest.fn(() => {
            return [];
          })
        },
        actions: {}
      }
    }
  });

  const mountFunction = (options: any) => {
    return mount(AddTeam, {
      store,
      vuetify,
      localVue,
      sync: false,
      mocks: { $t: jest.fn(() => {}) }, // tslint:disable-line
      ...options
    });
  };

  it('renders props when passed', () => {
    wrapper = mountFunction({});
    expect(wrapper.element).toMatchSnapshot();
  });

  // it('submit form on onlick ', () => {
  //   wrapper = mountFunction({});

  //   const addTeam = jest.fn();
  //   const button = wrapper.find('.submit-team');
  //   wrapper.vm.$on('action-btn:clicked', addTeam);
  //   button.trigger('click');

  //   expect(wrapper.element).toMatchSnapshot();
  // });
});
