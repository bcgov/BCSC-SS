import { mount } from '@vue/test-utils';
import ClientID from '@/components/CreateApp/ClientID.vue';
import Vuetify from 'vuetify';
import Vuex from 'vuex';
let vuetify: any;
vuetify = new Vuetify();

describe('ClientID.vue', () => {
  const store = new Vuex.Store({
    modules: {
      ClientIdModule: {
        namespaced: true,
        state: {},
        getters: {
          isLoading: jest.fn(),
          getApiData: jest.fn(() => {
            return {
              clientId: 'abcd',
              clientSecret: 'test',
              testUserAccounts: [
                {
                  userName: 'test user',
                  idKey: 'test id key'
                },
                {
                  userName: 'test user',
                  idKey: 'test id key'
                }
              ]
            };
          }),
          errorStatus: jest.fn()
        },
        actions: {
          getClientIdDetails: jest.fn()
        }
      }
    }
  });

  const mountFunction = (options: any) => {
    return mount(ClientID, {
      store,
      vuetify,
      mocks: { $t: jest.fn(() => {}), $copyText: jest.fn(() => {}) }, // tslint:disable-line
      ...options
    });
  };

  it('renders props when passed with gettors', () => {
    const ClientDetails = mountFunction({});
    expect(ClientDetails.element).toMatchSnapshot();
  });

  it('renders props when passed with gettors', () => {
    const ClientDetails = mountFunction({});
    ClientDetails.find('.client-id-copy').trigger('click');
    expect(ClientDetails.element).toMatchSnapshot();
  });
});
