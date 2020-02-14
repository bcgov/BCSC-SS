<template>
  <div class="home">
    <Dashboard :step="step" :id="id" />
  </div>
</template>

<script lang="ts">
// @ is an alias to /src
import { Component, Vue, Prop } from 'vue-property-decorator';
import Dashboard from '@/components/Dashboard/Dashboard.vue';

@Component({
  components: {
    Dashboard
  }
})
export default class DashboardHome extends Vue {
  @Prop({ default: 'info' })
  public step!: string;
  @Prop({ default: '' })
  public id!: string;
}
</script>
