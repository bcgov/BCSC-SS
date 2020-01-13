<template>
  <div class="home">
    <CreateApp />
  </div>
</template>

<script>
// @ is an alias to /src
import { Component, Vue } from 'vue-property-decorator';
import CreateApp from '@/components/CreateApp/CreateApp.vue';

@Component({
  components: {
    CreateApp
  }
})
// Home goes here
export default class Home extends Vue {}
</script>
