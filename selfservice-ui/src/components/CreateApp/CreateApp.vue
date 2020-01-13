/** * Footer of app */

<template>
  <div>Create App</div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import Input from '@/Atomic/Input/Input.vue';

@Component({
  components: {
    Input
  }
})
export default class Footer extends Vue {
  private e6: number = 0;
}
</script>

<style lang="scss" scoped>
@import './../../assets/styles/theme.scss';
</style>
