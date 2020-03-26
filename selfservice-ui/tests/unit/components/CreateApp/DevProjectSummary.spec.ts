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
    return mount(DevProjectSummary, {
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

  // it('show modal on click', () => {
  //   const DevProjectSummary = mountFunction({});

  //   DevProjectSummary.setData({ isLoading: false });
  //   const button = DevProjectSummary.find('.submit-package');
  //   DevProjectSummary.vm.$on('action-btn:clicked', jest.fn());
  //   button.trigger('click');
  //   expect(DevProjectSummary.element).toMatchSnapshot();
  // });
});

// describe('DevProjectSummary.vue', () => {
//   it('renders props when passed', () => {
//     const store = new Vuex.Store({
//       modules: {
//         ProjectInfoModule: {
//           namespaced: true,
//           state: {},
//           getters: {
//             getSingleProjectInfo: jest.fn(),
//             errorStatus: jest.fn(),
//             getFinalProjectSubmissionStatus: jest.fn()
//           },
//           actions: {
//             loadSingleProjectInfo: jest.fn()
//           }
//         },
//         TechnicalReqModule: {
//           namespaced: true,
//           state: {},
//           getters: {
//             getTechnicalReq: jest.fn(),
//             errorStatus: jest.fn()
//           },
//           actions: {
//             loadTechnicalReqDetails: jest.fn()
//           }
//         },
//         PackageAndTestModule: {
//           namespaced: true,
//           state: {},
//           getters: {
//             successStatus: jest.fn(),
//             getPackageList: jest.fn()
//           },
//           actions: {
//             loadPackage: jest.fn()
//           }
//         },
//         SharedModule: {
//           namespaced: true,
//           state: {},
//           getters: {
//             isRedirectFromSummaryPage: jest.fn()
//           },
//           actions: {
//             redirectFromSummaryPage: jest.fn()
//           }
//         }
//       }
//     });
//     const DevProjectSummary = shallowMount(DevProjectSummary, {
//       vuetify,
//       store,
//       mocks: { $t: jest.fn(() => {}) } // tslint:disable-line
//     });

//     expect(DevProjectSummary.element).toMatchSnapshot();
//   });
// });
