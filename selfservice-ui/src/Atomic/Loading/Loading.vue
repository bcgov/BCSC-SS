<template>
  <v-container>
    <v-layout d-flex align-center justify-center row wrap>
      <div col="4" class="mt-10">
        <v-progress-linear class="loading" indeterminate rounded height="6"></v-progress-linear>We know waiting sucks
        <br />but trust me it’s worth it
      </div>
    </v-layout>
  </v-container>
</template>
<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
@Component
export default class Loading extends Vue {}
</script>

<style lang="scss" scoped>
@import '@/assets/styles/theme.scss';
.loading {
  color: $BCgovGold5;
}
</style>
