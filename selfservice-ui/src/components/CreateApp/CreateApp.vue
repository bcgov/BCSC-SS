/** * CreateApp of app */

<template>
  <div>
    <AddProjectInfo v-if="step === 'info'" :id="id" />
    <AddTeam v-if="step === 'team'" :id="id" />
    <AddTechnicalReq v-if="step === 'technical'" :id="id" />
    <PackageSelect v-if="step === 'package'" :id="id" />
    <TestAccountRequest v-if="step === 'test-account'" :id="id" />
    <ClientID v-if="step === 'api-key'" :id="id" />
  </div>
</template>

<script lang="ts">
import { Component, Vue, Prop } from 'vue-property-decorator';
import AddProjectInfo from '@/components/CreateApp/AddProjectInfo.vue';
import AddTeam from '@/components/CreateApp/AddTeam.vue';
import AddTechnicalReq from '@/components/CreateApp/AddTechnicalReq.vue';
import PackageSelect from '@/components/CreateApp/PackageSelect.vue';
import TestAccountRequest from '@/components/CreateApp/TestAccountRequest.vue';
import ClientID from '@/components/CreateApp/ClientID.vue';

@Component({
  components: {
    AddProjectInfo,
    AddTeam,
    AddTechnicalReq,
    PackageSelect,
    TestAccountRequest,
    ClientID
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
