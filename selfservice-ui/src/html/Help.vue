<template>
  <div v-html="helpHtml" />
 </template>
<script lang="ts">
import helpHtml from 'html-loader!./Help.html';
import { Vue } from 'vue-property-decorator';
export default class Help extends Vue {
  public helpHtml : helpHtml;
}
</script>
<style lang="scss">
@import './../assets/styles/theme.scss';
</style>
