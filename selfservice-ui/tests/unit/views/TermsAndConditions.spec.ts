import { shallowMount, createLocalVue } from '@vue/test-utils';
import TermsAndConditions from '@/views/TermsAndConditions.vue';
import vuetify from 'vuetify';

describe('TermsAndConditions.vue', () => {
  let wrapper: any;
  beforeEach(() => {
    const localVue = createLocalVue();
    localVue.use(vuetify);

    wrapper = shallowMount(TermsAndConditions, {
      localVue,
    });
  });

  it('renders props when passed', () => {
    expect(wrapper.element).toMatchSnapshot();
  });
});
