<template>
  <div v-html="helpHtml" />
</template>
<script lang="ts">
const helpHtml = require('./HelpDev.html'); // tslint:disable-line
import { Vue } from 'vue-property-decorator';
export default class Help extends Vue {
  public helpHtml: any = helpHtml;
}
</script>
<style lang="scss">
@import './../assets/styles/theme.scss';
</style>
