/** * CreateApp of app */

<template>
  <div>
    <AddTechnicalReq v-if="step === 'technical'" :id="id" />
    <AddProjectInfo v-if="step === 'projectinfo'" />
  </div>
</template>

<script lang="ts">
import { Component, Vue, Prop } from 'vue-property-decorator';
import AddProjectInfo from '@/components/CreateApp/AddProjectInfo.vue';
import AddTechnicalReq from '@/components/CreateApp/AddTechnicalReq.vue';

@Component({
  components: {
    AddProjectInfo,
    AddTechnicalReq
  }
})
export default class CreateApp extends Vue {
  @Prop({ default: 'projectinfo' })
  public step!: string;
  @Prop({ default: 0 })
  public id!: number;
  private e6: number = 0;
}
</script>

<style lang="scss" scoped>
@import './../../assets/styles/theme.scss';
</style>
