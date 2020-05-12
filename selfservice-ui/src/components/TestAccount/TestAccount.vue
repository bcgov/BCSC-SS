/** * TestAccount component */

<template>
  <v-card class="mx-auto outer-card">
    <v-toolbar flat class="bc-subtitle padding-0" dark>
      <v-toolbar-title>{{ $t('testAccountList.pagetitle') }}</v-toolbar-title>
      <div class="flex-grow-1"></div>
    </v-toolbar>
    <v-divider></v-divider>
    <v-container>
      <v-row class="ma-5">
        <v-col cols="12" v-if="isLoading">
          <Loading />
        </v-col>

        <v-col
          cols="4"
          class="d-flex align-end flex-column-reverse mb-2"
          v-show="!isLoading"
        >
          <!-- <ProjectActions :id="id" /> -->
        </v-col>

        <v-col cols="12">
          <v-tabs slider-color="d-none" v-model="selectedTab">
            <v-tab class="font-weight-bold">
              {{ $t('testAccountList.tabAddtestAccount') }}
            </v-tab>
            <v-tab class="font-weight-bold">
              {{ $t('testAccountList.tabProjectUsage') }}
            </v-tab>
            <v-tab class="font-weight-bold">
              {{ $t('testAccountList.tabViewCardInfo') }}
            </v-tab>
            <div class="remaining-acc"><RemaingAccounts /></div>
            <v-tab-item class="custom-tabs-items">
              <v-card flat>
                <v-card-text>
                  <AddTestAccount />
                </v-card-text>
              </v-card>
            </v-tab-item>
            <v-tab-item class="custom-tabs-items">
              <v-card flat>
                <v-card-text>
                  {{ $t('testAccountList.tabProjectUsage') }}
                  <!-- <TeamRoles :id="id" /> -->
                </v-card-text>
              </v-card>
            </v-tab-item>

            <v-tab-item class="custom-tabs-items">
              <v-card flat>
                <v-card-text>
                  <p>{{ $t('testAccountList.tabViewCardInfo') }}</p>
                </v-card-text>
              </v-card>
            </v-tab-item>
            <v-tab-item class="custom-tabs-items">
              <v-card flat>
                <v-card-text>
                  <p>Security</p>
                </v-card-text>
              </v-card>
            </v-tab-item>
            <v-tab-item class="custom-tabs-items">
              <v-card flat>
                <v-card-text>
                  <p>Communications</p>
                </v-card-text>
              </v-card>
            </v-tab-item>
            <v-tab-item class="custom-tabs-items">
              <v-card flat>
                <v-card-text>
                  <p>Agreements</p>
                </v-card-text>
              </v-card>
            </v-tab-item>
            <v-tab-item class="custom-tabs-items">
              <v-card flat>
                <v-card-text>
                  <p>Prod access request</p>
                </v-card-text>
              </v-card>
            </v-tab-item>
          </v-tabs>
        </v-col>
      </v-row>
    </v-container>
  </v-card>
</template>
<script lang="ts">
import { Component, Vue, Watch, Prop } from 'vue-property-decorator';
import { Getter, namespace, Action } from 'vuex-class';
// import Button from '@/Atomic/Button/Button.vue';
// import TextArea from '@/Atomic/TextArea/TextArea.vue';
// import Alert from '@/Atomic/Alert/Alert.vue';

import AddTestAccount from '@/components/TestAccount/AddTestAccount.vue';
import RemaingAccounts from '@/components/TestAccount/RemaingAccounts.vue';

const TestAccountModule = namespace('TestAccountModule');

@Component({
  components: {
    AddTestAccount,
    RemaingAccounts,
  },
})
export default class TestAccount extends Vue {
  @TestAccountModule.Getter('isLoading')
  public isLoading!: boolean;
  private selectedTab: number = 0;
}
</script>

<style lang="scss" scoped>
@import './../../assets/styles/theme.scss';
.custom-tabs-items {
  border: 1px solid $gray5;
  min-height: 300px; // temp fix
}
.v-tab {
  color: $BCgovFontColorInvertedDark !important;
}
.v-tab--active {
  border: 1px solid $gray5;
  background-color: $BCgovGold5;
  color: $BCgovWhite !important;
}
.tab-headline {
  color: $BCgovFontColorInvertedDark;
}
.remaining-acc {
  width: 51%;
  text-align: right;
}
</style>
