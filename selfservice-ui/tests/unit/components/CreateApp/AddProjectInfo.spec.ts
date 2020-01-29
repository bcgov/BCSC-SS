import { shallowMount, createLocalVue } from '@vue/test-utils';
import AddProjectInfo from '@/components/CreateApp/AddProjectInfo.vue';
import vuetify from 'vuetify';
import Vuex from 'vuex';

describe('AddProjectInfo.vue', () => {
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
          }
        }
      }
    });
    wrapper = shallowMount(AddProjectInfo, {
      localVue,
      store,
      mocks: { $t: jest.fn(() => {}) } // tslint:disable-line
    });
  });

  it('renders props when passed', () => {
    expect(wrapper.element).toMatchSnapshot();
  });
});
