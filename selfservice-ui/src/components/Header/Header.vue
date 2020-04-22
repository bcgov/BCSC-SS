/** * Header of app */

<template>
  <div>
    <!-- <v-app-bar app> -->

    <v-app-bar app color class="header" light clipped-left>
      <!-- <v-app-bar-nav-icon
        @click.stop="drawer = !drawer"
        dark
      ></v-app-bar-nav-icon>-->
      <!-- <div class="banner"> -->
      <img
        src="@/assets/images/bc-logo-horizontal.svg"
        alt="Go to the Government of British Columbia website"
        class="img side-left-margin"
      />

      <v-toolbar-title>{{ $t('main.siteTitle') }}</v-toolbar-title>
      <sup aria-label="This application is currently in Beta phase" class="beta-phase-banner">Beta</sup>

      <v-spacer></v-spacer>
      <v-spacer></v-spacer>

      <v-btn
        text
        to="/dashboard"
        link
        dark
        class="d-none d-sm-flex login-btn side-right-margin"
        v-if="!isLoggedin"
      >Login</v-btn>

      <v-toolbar-title v-if="isLoggedin" class="d-flex">
        <v-btn icon dark large @click="$router.push(`/profile`)">
          <v-icon>mdi-account-edit</v-icon>
        </v-btn>
        <div class="profile-title">Welcome {{ userProfile.firstName }} {{ userProfile.lastName }}</div>
        <v-btn text @click="logout" color="white">
          <span class="mr-2 logout" color="white">Logout</span>
        </v-btn>
      </v-toolbar-title>
      <v-btn text to="/" link dark class="mr-2 d-sm-none toggleMenu" @click="toggleMenu">
        <v-icon>mdi-menu</v-icon>
      </v-btn>
    </v-app-bar>
    <nav class="navigation-main" :class="{ 'active-menu': showMenu }" id="navbar" v-if="!hideMenu">
      <ul>
        <li class="d-sm-none">
          <v-btn text to="/" link dark class="mr-2 login-btn">Login</v-btn>
        </li>
        <li v-for="item in items" :key="item.title">
          <router-link :to="item.link" v-if="checkRole(item)">
            {{
            item.title
            }}
          </router-link>
        </li>
      </ul>
    </nav>
    <!-- <template class="abcd" :class="{ 'active-menu': showMenu }">
      <Sidebar v-if="hideMenu" :drawer="drawer" />
    </template>-->
  </div>
</template>

<script lang="ts">
import { Component, Vue, Prop, Watch } from 'vue-property-decorator';
import { Getter, namespace, Action } from 'vuex-class';
import Sidebar from './Sidebar.vue';
const KeyCloakModule = namespace('KeyCloakModule');

@Component({
  components: {
    Sidebar
  }
})
export default class Header extends Vue {
  @Prop({ default: false }) private hideMenu!: boolean;

  @KeyCloakModule.Getter('userProfile') private userProfile!: [];
  @KeyCloakModule.Action('setLogout') private setLogout!: any;
  @KeyCloakModule.Getter('isLoggedin') private isLoggedin!: boolean;
  @KeyCloakModule.Getter('isAdmin')
  private isAdmin!: any;

  private showMenu: boolean = false;
  private drawer: boolean = false;
  private hideMenuInPage: boolean = !this.hideMenu;
  private items: any = [
    { title: 'Home', icon: 'mdi-home', link: '/' },
    { title: 'Dashboard', link: '/dashboard' },
    { title: 'Help', link: '/help' },
    {
      title: 'Load test accounts',
      link: '/add-test-account',
      roles: 'isAdmin'
    }
  ];

  @Watch('$route', { immediate: true, deep: true })
  private onUrlChange(newVal: any) {
    const { hideMenu = false } = newVal.meta;
    this.hideMenuInPage = !hideMenu || false;
  }
  /**
   * toggleMenu
   * @description : toggling mobile menu
   */
  private toggleMenu() {
    this.showMenu = !this.showMenu;
  }

  /**
   * make user logout
   * @returns {} dispatch
   */
  private logout() {
    this.setLogout();
  }
  private checkRole(data: any) {
    if (data && data.roles) {
      if (data.roles === 'isAdmin') {
        return this.isAdmin;
      }
    }
    return true;
  }
}
</script>

<style lang="scss" scoped>
@import './../../assets/styles/theme.scss';

.header {
  background-color: $BCgovBlue5 !important;
  border-bottom: 2px solid $BCgovGold5;
  border-color: $BCgovGold5 !important;
  color: $BCgovWhite;
  top: 0px;
  width: 100%;

  .img {
    width: 175px;
  }
}

.v-toolbar__title {
  color: $BCgovWhite;
}

.navigation-main {
  display: none;
  position: fixed;
  top: 65px;
  color: $BCgovGold5;
  background-color: $BCgovBlue10;
  width: 100%;
  -webkit-box-shadow: 0 6px 8px -4px #b3b1b3;
  -moz-box-shadow: 0 6px 8px -4px #b3b1b3;
  box-shadow: 0 6px 8px -4px #b3b1b3;
  padding: 10px 0 10px 0;
  z-index: 1;
  //   margin-left: -16px;
  @include sm {
    display: block;
    top: 56px;
  }

  ul {
    display: flex;
    flex-direction: column;
    margin: 0;
    color: $BCgovWhite;
    list-style: none;
    @include sm {
      flex-direction: row;
      margin: 0 65px 0 65px;
    }
    li {
      margin: 5px 0;
      a {
        display: flex;
        font-size: 0.813em;
        font-weight: normal; /* 400 */
        color: $BCgovWhite;
        padding: 0 15px 0 15px;
        text-decoration: none;

        @include sm {
          border-right: 1px solid #9b9b9b;
        }
      }
    }
  }
}
.active-menu {
  display: block;
  top: 56px;
}

.navigation-main ul li a:hover {
  text-decoration: underline;
}

.navigation-main ul .router-link-exact-active {
  text-decoration: underline;
  font-weight: bold;
}

:focus {
  outline: 4px solid #3b99fc;
  outline-offset: 1px;
}
.login-btn {
  background-color: $BCgovGold5;
  color: $BCgovWhite;
  font-size: 18px;
}
.beta-phase-banner {
  color: $BCgovGold5;
  text-transform: uppercase;
  font-weight: 600;
  font-size: 16px;
  margin-left: 4px;
}

.profile-title {
  display: flex;
  align-self: center;
}
</style>
