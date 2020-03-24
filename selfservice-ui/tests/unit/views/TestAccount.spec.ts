import { shallowMount, createLocalVue } from '@vue/test-utils';
import TestAccount from '@/views/TestAccount.vue';
import vuetify from 'vuetify';

describe('TestAccount.vue', () => {
  let wrapper: any;
  beforeEach(() => {
    const localVue = createLocalVue();
    localVue.use(vuetify);

    wrapper = shallowMount(TestAccount, {
      localVue
    });
  });

  it('renders props when passed', () => {
    expect(wrapper.element).toMatchSnapshot();
  });
});
