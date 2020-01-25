<template>
  <div class="home">
    <CreateApp :step="step" :id="id" />
  </div>
</template>

<script lang="ts">
// @ is an alias to /src
import { Component, Vue, Prop } from 'vue-property-decorator';
import CreateApp from '@/components/CreateApp/CreateApp.vue';

@Component({
  components: {
    CreateApp
  }
})
export default class CreateAppHome extends Vue {
  @Prop({ default: 'info' })
  public step!: string;
  @Prop({ default: '' })
  public id!: string;
}
</script>
