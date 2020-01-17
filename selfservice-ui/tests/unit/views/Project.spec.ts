import { shallowMount, createLocalVue } from '@vue/test-utils';
import Project from '@/views/Project.vue';
import vuetify from 'vuetify';

describe('Project.vue', () => {
  let wrapper: any;
  beforeEach(() => {
    const localVue = createLocalVue();
    localVue.use(vuetify);

    wrapper = shallowMount(Project, {
      localVue
    });
  });

  it('renders props when passed', () => {
    expect(wrapper.element).toMatchSnapshot();
  });
});
