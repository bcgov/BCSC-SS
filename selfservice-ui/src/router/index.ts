import Vue from 'vue';
import VueRouter from 'vue-router';
import KeycloakService from '@/services/keycloakservice';
import store from '@/store';
import Home from '../views/Home.vue';
import Unauthorized from '../views/Unauthorized.vue';
import PageNotFound from '../views/PageNotFound.vue';

Vue.use(VueRouter);

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      meta: { hideMenu: true },
      component: Home,
      props: true
    },
    {
      path: '/login',
      name: 'login',
      meta: { requiresAuth: true, roles: ['ss_admin', 'ss_client'] },
      component: () =>
        import(/* webpackChunkName: "Authorize" */ '../views/Authorize.vue')
    },
    {
      path: '/about',
      name: 'about',
      meta: { requiresAuth: true, roles: ['ss_client', 'ss_admin'] },
      props: true,
      component: () =>
        import(/* webpackChunkName: "About" */ '../views/About.vue')
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      meta: { requiresAuth: true, roles: ['ss_client', 'ss_admin'] },
      props: true,
      component: () =>
        import(/* webpackChunkName: "dashboard" */ '../views/Dashboard.vue')
    },
    {
      path: '/profile/:step?',
      name: 'profile',
      meta: { requiresAuth: true, roles: ['ss_client', 'ss_admin'] },
      props: true,
      component: () =>
        import(/* webpackChunkName: "profile" */ '../views/Profile.vue')
    },
    {
      path: '/add-test-account',
      name: 'testaccount',
      meta: { requiresAuth: true, roles: ['ss_admin'] },
      props: true,
      component: () =>
        import(/* webpackChunkName: "testaccount" */ '../views/TestAccount.vue')
    },
    {
      path: '/project/info',
      name: 'project-info',
      meta: { requiresAuth: true, roles: ['ss_client', 'ss_admin'] },
      props: true,
      component: () =>
        import(/* webpackChunkName: "project" */ '../views/Project.vue')
    },
    {
      path: '/project/:id?/:step?',
      name: 'project',
      meta: { requiresAuth: true, roles: ['ss_client', 'ss_admin'] },
      props: true,
      component: () =>
        import(/* webpackChunkName: "project" */ '../views/Project.vue')
    },
    {
      path: '/project-container/:id?/:tab?',
      name: 'projectcontainer',
      meta: { requiresAuth: true, roles: ['ss_client', 'ss_admin'] },
      props: true,
      component: () =>
        import(
          /* webpackChunkName: "projectcontainer" */ '../views/ProjectContainer.vue'
        )
    },

    {
      path: '/unauthorized',
      name: 'Unauthorized',
      meta: { requiresAuth: false },
      props: true,
      component: Unauthorized
    },
    { path: '*', meta: { requiresAuth: false }, component: PageNotFound }
  ]
});

router.beforeEach((to, from, next) => {
  // redirect to login page if not logged in and trying to access a restricted page
  // check login status

  const isLoggedin = store.state.KeyCloakModule.authenticated;
  if (to.meta.requiresAuth) {
    if (isLoggedin) {
      if (!store.state.KeyCloakModule.isVerfied && to.name !== 'profile') {
        next({
          path: '/profile/complete'
        });
        // }
      } else if (KeycloakService.checkPermission(to.meta.roles)) {
        next();
      } else {
        next({ name: 'Unauthorized' });
      }
    } else if (to.name === 'login') {
      const { redirect = '/login' } = to.params;
      KeycloakService.init(next, redirect, to.meta.roles, '/login');
    } else if (sessionStorage.getItem('keycloak_token')) {
      KeycloakService.init(next, to.path, to.meta.roles);
    } else {
      next({
        name: 'login',
        params: { redirect: to.path }
      });
    }
  } else {
    next();
  }
});

export default router;
