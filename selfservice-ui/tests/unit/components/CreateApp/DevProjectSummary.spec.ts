import { shallowMount, mount } from '@vue/test-utils';
import DevProjectSummary from '@/components/CreateApp/DevProjectSummary.vue';
import Vuetify from 'vuetify';
import Vuex from 'vuex';
let vuetify: any;
vuetify = new Vuetify();

describe('DevProjectSummary.vue', () => {
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
      }
    }
  });

  const mountFunction = (options: any) => {
    return shallowMount(DevProjectSummary, {
      store,
      vuetify,
      mocks: { $t: jest.fn(() => {}) }, // tslint:disable-line
      ...options
    });
  };

  it('renders props when passed with gettors', () => {
    const DevProjectSummaryPage = mountFunction({});

    expect(DevProjectSummaryPage.element).toMatchSnapshot();
  });
});
