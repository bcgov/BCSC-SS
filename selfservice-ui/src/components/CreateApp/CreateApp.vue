/** * CreateApp of app */

<template>
  <div>
    <AddProjectInfo />
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import AddProjectInfo from '@/components/CreateApp/AddProjectInfo.vue';

@Component({
  components: {
    AddProjectInfo
  }
})
export default class CreateApp extends Vue {
  private e6: number = 0;
}
</script>

<style lang="scss" scoped>
@import './../../assets/styles/theme.scss';
</style>
