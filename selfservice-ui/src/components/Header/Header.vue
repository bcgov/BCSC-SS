/** * Header of app */
<template>
  <div>
    <v-app-bar app color class="header" light clipped-left>
      <img
        src="@/assets/images/bc-logo-horizontal.svg"
        :alt="$t('header.labelLogoImageAlt')"
        class="img side-left-margin"
        tabindex="0"
      />
      <v-toolbar-title>{{ $t('header.siteTitle') }}</v-toolbar-title>
      <sup
        :aria-label="$t('header.ariaLabelBeta')"
        class="beta-phase-banner"
      >{{$t('header.labelBeta')}}</sup>
      <div id="access">
        <a class="skip-main" href="#main">Skip to main content</a>
      </div>
      <v-spacer></v-spacer>

      <Button
        text
        to="/dashboard"
        link
        dark
        :yellowBtn="true"
        class="d-none d-sm-flex login-btn side-right-margin"
        v-if="!isLoggedin"
        tabindex="0"
      >{{$t('header.labelLogin')}}</Button>

      <v-toolbar-title v-if="isLoggedin" class="d-flex">
        <v-btn
          icon
          dark
          large
          @click="$router.push(`/profile`)"
          @keyup.enter="$router.push(`/profile`)"
          class="icon-btn"
          :aria-label="$t('header.ariaLabelEditProfile')"
        >
          <v-icon>mdi-account-edit</v-icon>
        </v-btn>
        <div
          class="profile-title"
        >{{$t('header.labelWelcome')}} {{ userProfile.firstName }} {{ userProfile.lastName }}</div>
        <v-btn text @click="logout" @keyup.enter="logout" color="white" class="icon-btn">
          <span class="mr-2 logout" color="white">{{$t('header.labelLogout')}}</span>
        </v-btn>
      </v-toolbar-title>
      <v-btn text to="/" link dark class="mr-2 d-sm-none toggleMenu" @click="toggleMenu">
        <v-icon>mdi-menu</v-icon>
      </v-btn>
    </v-app-bar>
    <nav class="navigation-main" :class="{ 'active-menu': showMenu }" id="navbar" v-if="!hideMenu">
      <ul>
        <li class="d-sm-none">
          <v-btn text to="/" link dark class="mr-2 login-btn">{{$t('header.labelLogin')}}</v-btn>
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
  </div>
</template>

<script lang="ts">
import { Component, Vue, Prop, Watch } from 'vue-property-decorator';
import { Getter, namespace, Action } from 'vuex-class';
import Sidebar from './Sidebar.vue';
import Button from '@/Atomic/Button/Button.vue';

const KeyCloakModule = namespace('KeyCloakModule');

@Component({
  components: {
    Sidebar,
    Button
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

#access a {
  margin: 5px 0 0 -5000px;
  width: 200px;
  padding: 5px;
  position: absolute;
  top: 15px;
  color: #fcba19;
  &:focus,
  &:active {
    margin-left: 0;
  }
}
</style>
