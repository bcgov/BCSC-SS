/** * CreateApp of app */

<template>
  <div>
    <AddTechnicalReq v-if="step === 'technical'" :id="id" />
    <AddProjectInfo v-if="step === 'info'" :id="id" />
    <PackageSelect v-if="step === 'package'" :id="id" />
    <TestAccountRequest v-if="step === 'test-account'" :id="id" />
    <ProjectSummary v-if="step === 'summary'" :id="id" />
  </div>
</template>

<script lang="ts">
import { Component, Vue, Prop } from 'vue-property-decorator';
import AddProjectInfo from '@/components/CreateApp/AddProjectInfo.vue';
import AddTechnicalReq from '@/components/CreateApp/AddTechnicalReq.vue';
import PackageSelect from '@/components/CreateApp/PackageSelect.vue';
import TestAccountRequest from '@/components/CreateApp/TestAccountRequest.vue';
import ProjectSummary from '@/components/CreateApp/ProjectSummary.vue';

@Component({
  components: {
    AddProjectInfo,
    AddTechnicalReq,
    PackageSelect,
    TestAccountRequest,
    ProjectSummary
  }
})
export default class CreateApp extends Vue {
  @Prop({ default: 'info' })
  public step!: string;
  @Prop({ default: '' })
  public id!: number;
  private e6: number = 0;
}
</script>

<style lang="scss" scoped>
@import './../../assets/styles/theme.scss';
</style>
