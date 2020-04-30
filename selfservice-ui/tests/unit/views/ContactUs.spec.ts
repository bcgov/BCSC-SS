import { shallowMount, createLocalVue } from '@vue/test-utils';
import ContactUs from '@/views/ContactUs.vue';
import vuetify from 'vuetify';

describe('ContactUs.vue', () => {
  let wrapper: any;
  beforeEach(() => {
    const localVue = createLocalVue();
    localVue.use(vuetify);

    wrapper = shallowMount(ContactUs, {
      localVue,
    });
  });

  it('renders props when passed', () => {
    expect(wrapper.element).toMatchSnapshot();
  });
});
