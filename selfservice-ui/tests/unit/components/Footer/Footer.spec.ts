import { shallowMount, createLocalVue } from '@vue/test-utils';
import Footer from '@/components/Footer/Footer.vue';
import vuetify from 'vuetify';

describe('Footer.vue', () => {
  let wrapper: any;
  beforeEach(() => {
    const localVue = createLocalVue();
    localVue.use(vuetify);

    wrapper = shallowMount(Footer, {
      localVue,
      mocks: { $t: jest.fn(() => {}) }, // tslint:disable-line
    });
  });

  it('renders props when passed', () => {
    expect(wrapper.element).toMatchSnapshot();
  });
});
