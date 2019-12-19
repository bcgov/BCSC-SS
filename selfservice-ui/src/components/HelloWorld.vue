<template>
  <div class="hello">
    <h1>{{ msg }} <v-icon color="green">mdi-face</v-icon></h1>
    <h2>{{ devmsg }}<v-icon color="red">mdi-heart</v-icon></h2>
  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator';

@Component
export default class HelloWorld extends Vue {
  @Prop() private msg!: string;
  @Prop() private devmsg!: string;
}
</script>
