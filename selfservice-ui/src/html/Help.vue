<template>
  <div>
    <div v-html="helpHtml" v-if="page === 'help'" />
    <div v-html="helpDevHtml" v-if="page === 'help-dev'" />
    <div v-html="helpBCSCHtml" v-if="page === 'help-bcsc'" />
    <div v-html="helpHowToUseHtml" v-if="page === 'help-howto'" />
    <div v-html="helpIsForMeHtml" v-if="page === 'help-isforme'" />
    <div v-html="helpCreateProject" v-if="page === 'help-create-project'" />
    <div v-html="helpMoveThruProject" v-if="page === 'help-movethru-project'" />
    <div v-html="helpGoLive" v-if="page === 'help-go-live'" />
  </div>
</template>
<script lang="ts">
/* tslint:disable */
import { Component, Vue, Prop } from 'vue-property-decorator';

const helpHtml = require('./Help.html');
const helpDevHtml = require('./HelpDev.html');
const helpBCSCHtml = require('./HelpBCSC.html');
const helpHowToUseHtml = require('./HelpHowToUse.html');
const helpIsForMeHtml = require('./HelpIsForMe.html');
const helpCreateProject = require('./HelpCreateProject.html');
const helpMoveThruProject = require('./HelpMoveThruProject.html');
const helpGoLive = require('./HelpGoLive.html');

@Component
export default class Help extends Vue {
  @Prop({ default: 'help' })
  public page!: string;

  public helpHtml: any = helpHtml;
  public helpDevHtml: any = helpDevHtml;
  public helpBCSCHtml: any = helpBCSCHtml;
  public helpHowToUseHtml: any = helpHowToUseHtml;
  public helpIsForMeHtml: any = helpIsForMeHtml;
  public helpCreateProject: any = helpCreateProject;
  public helpMoveThruProject: any = helpMoveThruProject;
  public helpGoLive: any = helpGoLive;
}
</script>
<style lang="scss">
@import './../assets/styles/theme.scss';
</style>
