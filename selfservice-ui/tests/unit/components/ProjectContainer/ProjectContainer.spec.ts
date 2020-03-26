import { shallowMount, createLocalVue } from '@vue/test-utils';
import ProjectContainer from '@/components/ProjectContainer/ProjectContainer.vue';
import vuetify from 'vuetify';
import Vuex from 'vuex';

describe('ProjectContainer.vue', () => {
  let wrapper: any;
  beforeEach(() => {
    const localVue = createLocalVue();
    localVue.use(vuetify);
    const store = new Vuex.Store({
      modules: {
        ProjectInfoModule: {
          namespaced: true,
          state: {},
          getters: {
            getSingleProjectInfo: jest.fn(() => {
              return {
                description: 'test discription',
                id: 12,
                organizationName: 'new org',
                projectName: 'new project',
                users: [
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

    wrapper = shallowMount(ProjectContainer, {
      localVue,
      store,
      mocks: { $t: jest.fn(() => {}) } // tslint:disable-line
    });
  });

  it('renders props when passed', () => {
    expect(wrapper.element).toMatchSnapshot();
  });
});
