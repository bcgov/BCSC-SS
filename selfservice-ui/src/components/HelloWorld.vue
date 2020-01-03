<template>
  <div class="hello">
    <h1>
      {{ msg }}
      <v-icon color="green" v-if="msg && msg !== ''">mdi-face</v-icon>
    </h1>
    <h2>
      {{ devmsg }}
      <v-icon color="red" v-if="devmsg && devmsg !== ''">mdi-heart</v-icon>
    </h2>
  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator';
import Input from '@/Atomic/Input/Input.vue';

@Component
export default class HelloWorld extends Vue {
  @Prop() private msg!: string;
  @Prop() private devmsg!: string;
}
</script>
