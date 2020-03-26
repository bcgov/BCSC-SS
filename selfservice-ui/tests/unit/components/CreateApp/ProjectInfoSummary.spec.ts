import { shallowMount } from '@vue/test-utils';
import ProjectInfoSummary from '@/components/CreateApp/ProjectInfoSummary.vue';
import Vuetify from 'vuetify';
import Vuex from 'vuex';
let vuetify: any;
vuetify = new Vuetify();

describe('ProjectInfoSummary.vue', () => {
  const storeData = new Vuex.Store({
    modules: {
      ProjectInfoModule: {
        namespaced: true,
        state: {},
        getters: {
          getSingleProjectInfo: jest.fn(() => {
            return {
              description: 'discription',
              id: 11,
              organizationName: 'new org2',
              projectName: 'new project2',
              users: [
                {
                  email: 'e@e.com',
                  firstName: 'fname',
                  id: 2,
                  lastName: 'lname',
                  phone: '09870987654321',
                  role: 2
                },
                {
                  email: 'bb@test.com',
                  firstName: 'john',
                  id: 16,
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
          }),
          getFinalProjectSubmissionStatus: jest.fn(),
          errorStatus: jest.fn()
        },
        actions: {
          loadSingleProjectInfo: jest.fn()
        }
      }
    }
  });

  const mountFunction = (options: any) => {
    return shallowMount(ProjectInfoSummary, {
      store: storeData,
      vuetify,
      mocks: { $t: jest.fn(() => {}) }, // tslint:disable-line
      ...options
    });
  };

  it('renders props when passed with gettors', () => {
    const projectInfoSummary = mountFunction({});

    expect(projectInfoSummary.element).toMatchSnapshot();
  });
});
