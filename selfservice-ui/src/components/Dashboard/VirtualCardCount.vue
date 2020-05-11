/** * Dashboard of app */

<template>
  <v-card class="mx-auto">
    <v-toolbar flat class="bc-subtitle" dark>
      <v-toolbar-title>{{
        $t('dashboard.virtualCardCountTitle')
      }}</v-toolbar-title>
      <div class="flex-grow-1"></div>
    </v-toolbar>
    <v-divider></v-divider>
    <v-container>
      <v-row class="ma-2">
        <v-col cols="12" md="8">
          <RemaingAccounts />
        </v-col>
        <v-col cols="12" md="4">
          <div class="remaining-acc-btn">
            <Button
              class="white--text ml-3"
              depressed
              @click="$router.push(`/add-test-account`)"
              name="btn-create-project"
              data-test-id="btn-create-project"
              >{{ $t('dashboard.btnManageTestAccount') }}</Button
            >
          </div>
        </v-col>
      </v-row>
    </v-container>
  </v-card>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import { namespace } from 'vuex-class';

import Button from '@/Atomic/Button/Button.vue';
import RemaingAccounts from '@/components/TestAccount/RemaingAccounts.vue';

const TestAccountModule = namespace('TestAccountModule');

@Component({
  components: {
    Button,
    RemaingAccounts,
  },
})
export default class VirtualCardCount extends Vue {}
</script>

<style lang="scss" scoped>
@import './../../assets/styles/theme.scss';

.remaining-acc-btn {
  width: 250px;
  display: inline;
  float: right;
}
</style>
