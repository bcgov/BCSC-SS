<template>
  <v-app>
    <Header />
    <v-content>
      <v-container fluid class="main-content">
        <router-view />
      </v-container>
    </v-content>
    <Footer />
  </v-app>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import Header from '@/components/Header/Header.vue';
import Footer from '@/components/Footer/Footer.vue';

@Component({
  components: {
    Header,
    Footer
  }
})
export default class App extends Vue {}
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
