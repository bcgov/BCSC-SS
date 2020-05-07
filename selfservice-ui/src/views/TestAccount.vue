<template>
  <v-card flat>
    <TestAccount />
  </v-card>
</template>

<script>
// @ is an alias to /src
import { Component, Vue } from 'vue-property-decorator';
import TestAccount from '@/components/TestAccount/TestAccount.vue';

@Component({
  components: {
    TestAccount
  }
})
// Home goes here
export default class TestAccountPage extends Vue {}
</script>
