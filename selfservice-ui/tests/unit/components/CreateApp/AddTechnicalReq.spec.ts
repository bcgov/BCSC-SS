import { mount, createLocalVue } from '@vue/test-utils';
import AddTechnicalReq from '@/components/CreateApp/AddTechnicalReq.vue';
import Vuetify from 'vuetify';
import Vuex from 'vuex';
let vuetify: any;
vuetify = new Vuetify();

describe('AddTechnicalReq.vue', () => {
  let wrapper: any;
  const localVue = createLocalVue();

  localVue.use(Vuetify);
  localVue.use(Vuex);
  vuetify = new Vuetify();
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
          getSingleTechnicalReq: jest.fn(),
          loadSingleProjectInfo: jest.fn()
        }
      },
      TechnicalReqModule: {
        namespaced: true,
        state: {},
        getters: {
          getSingleTechnicalReq: jest.fn(),
          getTechnicalReq: jest.fn(),
          isLoading: jest.fn()
        },
        actions: {
          getSingleTechnicalReq: jest.fn(),
          addTechnicalReq: jest.fn()
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
    return mount(AddTechnicalReq, {
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

  it('renders props when passed', () => {
    wrapper = mountFunction({});
    const inputElement = wrapper.find('.addUri input');
    inputElement.element.value = 'value';
    inputElement.trigger('blur');

    expect(wrapper.element).toMatchSnapshot();
  });

  it('submit form on onlick ', () => {
    wrapper = mountFunction({});

    const addTechnicalReq = jest.fn();
    const button = wrapper.find('.submit-req');
    wrapper.vm.$on('action-btn:clicked', addTechnicalReq);
    button.trigger('click');

    expect(wrapper.element).toMatchSnapshot();
  });
});
