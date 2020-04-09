import { shallowMount, mount } from '@vue/test-utils';
import TeamSummary from '@/components/CreateApp/TeamSummary.vue';
import Vuetify from 'vuetify';
import Vuex from 'vuex';
let vuetify: any;
vuetify = new Vuetify();

describe('TeamSummary.vue', () => {

  const mountFunction = (options: any) => {
    return mount(TeamSummary, {
      propsData: {
        team: [
          {
            email: 'e@e.com',
            firstName: 'fname',
            id: 3,
            lastName: 'lname',
            phone: '09870987654321',
            role: 2
          },
          {
            email: 'bb@test.com',
            firstName: 'john',
            id: 2,
            lastName: 'bb',
            phone: '987654321',
            role: 3
          },
          {
            email: 'user@yopmail.com',
            firstName: 'John',
            id: 1,
            lastName: 'Doe',
            phone: '',
            role: 1
          }
        ]
      },
      vuetify,
      mocks: { $t: jest.fn(() => { }) }, // tslint:disable-line
      ...options
    });
  };

  it('renders props when passed with gettors', () => {
    const teamSummary = mountFunction({});

    expect(teamSummary.element).toMatchSnapshot();
  });
});

describe('TeamSummary.vue', () => {
  it('renders props when passed', () => {

    const teamSummary = shallowMount(TeamSummary, {
      propsData: {
        team: [
          {
            email: 'e@e.com',
            firstName: 'fname',
            id: 3,
            lastName: 'lname',
            phone: '09870987654321',
            role: 2
          },
          {
            email: 'bb@test.com',
            firstName: 'john',
            id: 2,
            lastName: 'bb',
            phone: '987654321',
            role: 3
          },
          {
            email: 'user@yopmail.com',
            firstName: 'John',
            id: 1,
            lastName: 'Doe',
            phone: '',
            role: 1
          }
        ]
      },
      vuetify,
      mocks: { $t: jest.fn(() => { }) } // tslint:disable-line
    });

    expect(teamSummary.element).toMatchSnapshot();
  });
});
