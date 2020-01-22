import { shallowMount, createLocalVue } from '@vue/test-utils';
import AddTechnicalReq from '@/components/CreateApp/AddTechnicalReq.vue';
import vuetify from 'vuetify';
import Vuex from 'vuex';

describe('AddTechnicalReq.vue', () => {
  let wrapper: any;
  beforeEach(() => {
    const localVue = createLocalVue();
    localVue.use(vuetify);
    localVue.use(Vuex);
    const store = new Vuex.Store({
      modules: {
        ProjectInfoModule: {
          namespaced: true,
          state: {},
          getters: {
            getSingleProjectInfo: jest.fn(),
            isLoggedin: jest.fn()
          },
          actions: { getSingleTechnicalReq: jest.fn() }
        },
        TechnicalReqModule: {
          namespaced: true,
          state: {},
          getters: {
            getSingleTechnicalReq: jest.fn()
          },
          actions: { getSingleTechnicalReq: jest.fn() }
        }
      }
    });
    wrapper = shallowMount(AddTechnicalReq, {
      localVue,
      store
    });
  });

  it('renders props when passed', () => {
    expect(wrapper.element).toMatchSnapshot();
  });
});
