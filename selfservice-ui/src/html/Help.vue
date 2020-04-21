<template>
  <div>
    <div v-html="helpHtml" v-if="page === 'help'" />
    <div v-html="helpDevHtml" v-if="page === 'help-dev'" />
  </div>
</template>
<script lang="ts">
/* tslint:disable */
import { Component, Vue, Prop } from 'vue-property-decorator';

const helpHtml = require('./Help.html');
const helpDevHtml = require('./HelpDev.html');

@Component
export default class Help extends Vue {
  @Prop({ default: 'help' })
  public page!: string;

  public helpHtml: any = helpHtml;
  public helpDevHtml: any = helpDevHtml;
}
</script>
<style lang="scss">
@import './../assets/styles/theme.scss';
</style>
