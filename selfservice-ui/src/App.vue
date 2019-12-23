<template>
  <v-app>
    <Header />
    <v-content>
      <v-container fluid class="main-content">
        <router-view />
      </v-container>
    </v-content>
  </v-app>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import Header from '@/components/Header/Header.vue';
@Component({
  components: {
    Header
  }
})
export default class App extends Vue {}
</script>

<style lang="scss">
#app {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  // margin-top: 60px;
}
.main-content {
  margin-top: 60px;
}
</style>
