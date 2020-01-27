import { mount, createLocalVue } from '@vue/test-utils';
import AddTechnicalReq from '@/components/CreateApp/AddTechnicalReq.vue';
import Vuetify from 'vuetify';
import Vuex from 'vuex';

describe('AddTechnicalReq.vue', () => {
  let vuetify: any;
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
          getSingleTechnicalReq: jest.fn()
        },
        actions: { getSingleTechnicalReq: jest.fn() }
      }
    }
  });

  const mountFunction = (options: any) => {
    return mount(AddTechnicalReq, {
      store,
      vuetify,
      localVue,
      ...options
    });
  };

  // // let wrapper: any;
  // beforeEach(() => {
  //   const localVue = createLocalVue();
  //   localVue.use(vuetify);
  //   localVue.use(Vuex);
  //   const store = new Vuex.Store({
  //     modules: {
  //       ProjectInfoModule: {
  //         namespaced: true,
  //         state: {},
  //         getters: {
  //           getSingleProjectInfo: jest.fn(),
  //           isLoggedin: jest.fn()
  //         },
  //         actions: {
  //           getSingleTechnicalReq: jest.fn(),
  //           loadSingleProjectInfo: jest.fn()
  //         }
  //       },
  //       TechnicalReqModule: {
  //         namespaced: true,
  //         state: {},
  //         getters: {
  //           getSingleTechnicalReq: jest.fn()
  //         },
  //         actions: { getSingleTechnicalReq: jest.fn() }
  //       }
  //     }
  //   });
  //   wrapper = shallowMount(AddTechnicalReq, {
  //     localVue,
  //     store
  //   });
  // });

  it('renders props when passed', () => {
    const wrapper = mountFunction({});
    expect(wrapper.element).toMatchSnapshot();
  });
});
