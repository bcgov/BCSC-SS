/* tslint:disable */
import { shallowMount, createLocalVue } from '@vue/test-utils';
import Sidebar from '@/components/Header/Sidebar.vue';
import vuetify from 'vuetify';

describe('Sidebar.vue', () => {
  let wrapper: any;
  beforeEach(() => {
    const localVue = createLocalVue();
    localVue.use(vuetify);

    wrapper = shallowMount(Sidebar, {
      localVue,
      mocks: { $t: jest.fn(() => {}) } // tslint:disable-line
    });
  });

  it('renders props when passed', () => {
    expect(wrapper.element).toMatchSnapshot();
  });
});
