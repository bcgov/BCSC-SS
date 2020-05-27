<template>
  <v-app>
    <Header :hideMenu="hideMenu" />
    <a class="anchor" id="top"></a>
    <v-content>
      <v-container fluid class="main-content" id="main">
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
  @Watch('$route', { immediate: true, deep: true })
  private onUrlChange(newVal: any) {
    const { hideMenu = false } = newVal.meta;
    this.hideMenu = hideMenu || false;
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
a.anchor {
  display: block;
  position: relative;
  top: -250px;
  visibility: hidden;
}
</style>
