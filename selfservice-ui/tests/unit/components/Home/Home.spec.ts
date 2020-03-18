import { shallowMount, createLocalVue } from '@vue/test-utils';
import Home from '@/components/Home/Home.vue';
import vuetify from 'vuetify';

describe('Home.vue', () => {
  let wrapper: any;
  beforeEach(() => {
    const localVue = createLocalVue();
    localVue.use(vuetify);

    wrapper = shallowMount(Home, {
      localVue,
      mocks: { $t: jest.fn(() => {}) } // tslint:disable-line
    });
  });

  it('renders props when passed', () => {
    expect(wrapper.element).toMatchSnapshot();
  });
});
