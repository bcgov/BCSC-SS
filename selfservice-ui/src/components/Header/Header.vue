/** * Header of app */

<template>
  <div>
    <!-- <v-app-bar app> -->
    <v-app-bar app color="" class="header" light="">
      <!-- <div class="banner"> -->
      <img
        src="@/assets/images/bc-logo-horizontal.svg"
        alt="Go to the Government of British Columbia website"
        class="img side-left-margin"
      />
      <!-- </a> -->
      <!-- <h1 class="text">BC SERVICE CARD</h1> -->
      <v-toolbar-title>BCSC SELF SERVICE</v-toolbar-title>
      <!-- </div> -->

      <v-spacer></v-spacer>
      <v-spacer></v-spacer>

      <v-btn
        text
        to="/"
        link
        dark
        class="d-none d-sm-flex login-btn side-right-margin"
        >Login</v-btn
      >
      <v-btn text to="/" link dark class="mr-2 d-sm-none" @click="toggleMenu">
        <v-icon>mdi-menu</v-icon>
      </v-btn>
    </v-app-bar>
    <nav
      class="navigation-main"
      :class="{ 'active-menu': showMenu }"
      id="navbar"
    >
      <ul>
        <li class="d-sm-none">
          <v-btn text to="/" link dark class="mr-2 login-btn">Login</v-btn>
        </li>
        <li>
          <router-link to="/">Home</router-link>
        </li>

        <li>
          <router-link to="about">About</router-link>
        </li>
      </ul>
    </nav>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';

@Component
export default class Header extends Vue {
  public showMenu: boolean = false;
  /**
   * toggleMenu
   * @description : toggling mobile menu
   */
  private toggleMenu() {
    this.showMenu = !this.showMenu;
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
    color: #fff;
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
        color: #fff;
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
}
</style>
