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
      component: Home
    },
    {
      path: '/login',
      name: 'login',
      meta: { requiresAuth: true, roles: ['ss_admin', 'ss_client', 'idir'] },
      component: () =>
        import(/* webpackChunkName: "Authorize" */ '../views/Authorize.vue')
    },
    {
      path: '/about',
      name: 'about',
      meta: { requiresAuth: true, roles: ['ss_client', 'idir', 'ss_admin'] },
      props: true,
      component: () =>
        import(/* webpackChunkName: "About" */ '../views/About.vue')
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
      meta: { requiresAuth: true, roles: ['ss_client', 'idir', 'ss_admin'] },
      props: true,
      component: () =>
        import(/* webpackChunkName: "project" */ '../views/Project.vue')
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
      if (KeycloakService.checkPermission(to.meta.roles)) {
        next();
      } else {
        next({ name: 'Unauthorized' });
      }
    } else if (sessionStorage.getItem('keycloak_token')) {
      KeycloakService.init(next, to.path, to.meta.roles);
      // debugger;
    } else {
      KeycloakService.init(next, '/login', to.meta.roles);
    }
  } else {
    next();
  }
});

export default router;
