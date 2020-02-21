import { shallowMount, createLocalVue } from '@vue/test-utils';
import Profile from '@/views/Profile.vue';
import vuetify from 'vuetify';

describe('Profile.vue', () => {
  let wrapper: any;
  beforeEach(() => {
    const localVue = createLocalVue();
    localVue.use(vuetify);

    wrapper = shallowMount(Profile, {
      localVue
    });
  });

  it('renders props when passed', () => {
    expect(wrapper.element).toMatchSnapshot();
  });
});
