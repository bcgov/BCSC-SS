import { shallowMount, createLocalVue } from '@vue/test-utils';
import ProjectContainer from '@/components/ProjectContainer/ProjectContainer.vue';
import vuetify from 'vuetify';

describe('ProjectContainer.vue', () => {
  let wrapper: any;
  beforeEach(() => {
    const localVue = createLocalVue();
    localVue.use(vuetify);

    wrapper = shallowMount(ProjectContainer, {
      localVue,
      mocks: { $t: jest.fn(() => {}) } // tslint:disable-line
    });
  });

  it('renders props when passed', () => {
    expect(wrapper.element).toMatchSnapshot();
  });
});
