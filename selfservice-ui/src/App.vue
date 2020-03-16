<template>
  <v-app>
    <Header :hideMenu="hideMenu" />
    <v-content>
      <v-container fluid class="main-content">
        <router-view />
      </v-container>
    </v-content>
    <Footer />
  </v-app>
</template>

<script lang="ts">
import { Component, Vue, Prop, Watch } from 'vue-property-decorator';
import Header from '@/components/Header/Header.vue';
import Footer from '@/components/Footer/Footer.vue';

@Component({
  components: {
    Header,
    Footer
  }
})
export default class App extends Vue {
  private hideMenu: boolean = false;
  constructor() {
    super();
  }

  private created() {
    const { hideMenu = false } = this.$route.meta;
    this.hideMenu = hideMenu || false;
  }
}
</script>

<style lang="scss">
@import './assets/styles/theme.scss';

#app {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
.main-content {
  margin-top: 10px;
  @include sm {
    margin-top: 56px;
  }
}
</style>
