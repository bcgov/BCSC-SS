<template>
  <div class="home">
    <HelloWorld msg="Hello world" />
  </div>
</template>

<script>
// @ is an alias to /src
import { Component, Vue } from 'vue-property-decorator';
import HelloWorld from '@/components/HelloWorld.vue';

@Component({
  components: {
    HelloWorld
  }
})
// Home goes here
export default class Home extends Vue {}
</script>
