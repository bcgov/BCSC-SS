<template>
  <div class="home">
    <ProjectContainer :tab="tab" :id="id" />
  </div>
</template>

<script lang="ts">
// @ is an alias to /src
import { Component, Vue, Prop } from 'vue-property-decorator';
import ProjectContainer from '@/components/ProjectContainer/ProjectContainer.vue';

@Component({
  components: {
    ProjectContainer,
  },
})
export default class ProjectContainerHome extends Vue {
  @Prop({ default: 'info' })
  public tab!: string;
  @Prop({ default: 0 })
  public id!: string;
}
</script>
