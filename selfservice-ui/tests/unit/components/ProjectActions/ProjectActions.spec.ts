import { mount } from '@vue/test-utils';
import ProjectActions from '@/components/ProjectActions/ProjectActions.vue';
import Vuetify from 'vuetify';
import Vuex from 'vuex';
import { singleProject } from '../../mocks/projectinfo';
let vuetify: any;
vuetify = new Vuetify();
describe('ProjectActions.vue', () => {
  const store = new Vuex.Store({
    modules: {
      ProjectInfoModule: {
        namespaced: true,
        state: {},
        getters: {
          getChangeStatus: jest.fn(() => {
            return { singleProject };
          }),
          getDeleteProjectReturn: jest.fn(),
          getSingleProjectInfo: jest.fn(),
        },
        actions: {
          loadSingleProjectInfo: jest.fn(),
          deleteProject: jest.fn(),
          updateProjectStatus: jest.fn(),
        },
      },
      KeyCloakModule: {
        namespaced: true,
        state: {},
        getters: {
          isAdmin: jest.fn(() => {
            return true;
          }),
        },
        actions: { setLogout: jest.fn() },
      },
    },
  });

  const mountFunction = (options: any) => {
    return mount(ProjectActions, {
      store,
      vuetify,
      mocks: { $t: jest.fn(() => {}) }, // tslint:disable-line
      ...options,
    });
  };

  it('renders props when passed', () => {
    const wrapper = mountFunction({});
    expect(wrapper.element).toMatchSnapshot();
  });

  it('renders props on click of Live access', () => {
    const projectActionPage = mountFunction({});
    const toggleDelete = jest.fn();
    projectActionPage.setData({ projectStatus: 2 });
    const button = projectActionPage.find('.btn-req');
    projectActionPage.vm.$on('action-btn:clicked', toggleDelete);
    button.trigger('click');

    expect(projectActionPage.element).toMatchSnapshot();
  });
  it('renders props when passed with gettors', () => {
    const projectActionPage = mountFunction({});
    const toggleDelete = jest.fn();
    projectActionPage.setData({ projectStatus: 1 });

    const button = projectActionPage.find('.btn-delete');
    projectActionPage.vm.$on('action-btn:clicked', toggleDelete);
    button.trigger('click');

    expect(projectActionPage.element).toMatchSnapshot();
  });

  it('renders props on click of delete', () => {
    const projectActionPage = mountFunction({});
    const toggleDelete = jest.fn();
    projectActionPage.setData({ deleteDialog: true });
    const button = projectActionPage.find('.dialog-delete');
    projectActionPage.vm.$on('action-btn:clicked', toggleDelete);
    button.trigger('click');

    expect(projectActionPage.element).toMatchSnapshot();
  });

  it('renders props on click of delete', () => {
    const projectActionPage = mountFunction({});
    const toggleDelete = jest.fn();
    projectActionPage.setData({ requestDialog: true });
    const button = projectActionPage.find('.btn-live');
    projectActionPage.vm.$on('action-btn:clicked', toggleDelete);
    button.trigger('click');

    expect(projectActionPage.element).toMatchSnapshot();
  });
});
