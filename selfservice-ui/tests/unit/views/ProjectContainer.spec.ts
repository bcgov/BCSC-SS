import { shallowMount, createLocalVue } from '@vue/test-utils';
import ProjectContainer from '@/views/ProjectContainer.vue';
import vuetify from 'vuetify';

describe('ProjectContainer.vue', () => {
  let wrapper: any;
  beforeEach(() => {
    const localVue = createLocalVue();
    localVue.use(vuetify);

    wrapper = shallowMount(ProjectContainer, {
      localVue
    });
  });

  it('renders props when passed', () => {
    expect(wrapper.element).toMatchSnapshot();
  });
});
