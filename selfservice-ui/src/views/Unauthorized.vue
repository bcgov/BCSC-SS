<template>
  <v-container>
    <v-layout d-flex align-center justify-center row wrap>
      <ErrorPage type="unauthorized" />
    </v-layout>
  </v-container>
</template>
<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import ErrorPage from '@/components/ErrorPage/ErrorPage.vue';

@Component({
  components: { ErrorPage }
})
export default class Authorize extends Vue {}
</script>
