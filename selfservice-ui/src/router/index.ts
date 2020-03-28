import Vue from 'vue';
import VueRouter from 'vue-router';
import KeycloakService from '@/services/keycloakservice';
import store from '@/store';
import Home from '../views/Home.vue';
import Unauthorized from '../views/Unauthorized.vue';
import PageNotFound from '../views/PageNotFound.vue';

Vue.use(VueRouter);

const metaAllRoles = { requiresAuth: true, roles: ['ss_admin', 'ss_client'] };

function createRoute(path: string, name: string, component: any, meta: any, props = true) {
  return {
    path,
    name,
    meta,
    component,
    props
  };
}

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    createRoute('/', 'home', Home, { hideMenu: true }),
    createRoute(
      '/login',
      'login',
      () => import(/* webpackChunkName: "Authorize" */ '../views/Authorize.vue'),
      metaAllRoles),
    createRoute(
      '/about',
      'about',
      () => import(/* webpackChunkName: "About" */ '../views/About.vue'),
      metaAllRoles),
    createRoute(
      '/dashboard',
      'dashboard',
      () => import(/* webpackChunkName: "dashboard" */ '../views/Dashboard.vue'),
      metaAllRoles),
    createRoute(
      '/profile/:step?',
      'profile',
      () => import(/* webpackChunkName: "profile" */ '../views/Profile.vue'),
      metaAllRoles),
    createRoute(
      '/project/info',
      'project-info',
      () => import(/* webpackChunkName: "project" */ '../views/Project.vue'),
      metaAllRoles),
    createRoute(
      '/project/:id?/:step?',
      'project',
      () => import(/* webpackChunkName: "project" */ '../views/Project.vue'),
      metaAllRoles),
    createRoute(
      '/project-container/:id?/:tab?',
      'projectcontainer',
      () => import(/* webpackChunkName: "projectcontainer" */ '../views/ProjectContainer.vue'),
      metaAllRoles),
    createRoute(
      '/add-test-account',
      'testaccount',
      () => import(/* webpackChunkName: "testaccount" */ '../views/TestAccount.vue'),
      { requiresAuth: true, roles: ['ss_admin'] }),
    createRoute(
      '/unauthorized',
      'Unauthorized',
      Unauthorized,
      { requiresAuth: false }),
    { path: '*', meta: { requiresAuth: false }, component: PageNotFound }
  ]
});

router.beforeEach((to, from, next) => {
  // redirect to login page if not logged in and trying to access a restricted page
  // check login status

  const isLoggedin = store.state.KeyCloakModule.authenticated;
  if (to.meta.requiresAuth) {
    if (isLoggedin) {
      if (
        !store.state.KeyCloakModule.isVerfied &&
        to.name !== 'profile'
      ) {
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
