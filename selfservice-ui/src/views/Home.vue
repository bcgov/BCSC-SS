<template>
  <v-card flat>
    <Home />
  </v-card>
</template>

<script>
// @ is an alias to /src
import { Component, Vue } from 'vue-property-decorator';
import Home from '@/components/Home/Home.vue';

@Component({
  components: {
    Home
  }
})
// Home goes here
export default class HomePage extends Vue {}
</script>
