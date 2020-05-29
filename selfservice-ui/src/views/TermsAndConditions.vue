<template>
  <div class="home text-left">
    <v-card class="mx-auto outer-card" flat>
      <TermsAndConditions />
    </v-card>
  </div>
</template>

<script lang="ts">
// @ is an alias to /src
import { Component, Vue, Prop } from 'vue-property-decorator';
import TermsAndConditions from '@/components/Profile/TermsAndConditions.vue';

@Component({
  components: {
    TermsAndConditions,
  },
})
export default class TermsAndConditionsHome extends Vue {}
</script>
