/** * TestAccount component */

<template>
  <v-card class="mx-auto outer-card">
    <v-toolbar flat class="bc-subtitle padding-0" dark>
      <v-btn icon @click="goBack()" :aria-label="$t('testAccountList.btnBack')">
        <v-icon>mdi-arrow-left</v-icon>
      </v-btn>
      <v-toolbar-title>{{ $t('testAccountList.pagetitle') }}</v-toolbar-title>
      <div class="flex-grow-1"></div>

      <div class="flex-grow-1"></div>
    </v-toolbar>
    <v-divider></v-divider>
    <v-item-group mandatory>
      <v-container>
        <v-row class="mx-4">
          <v-col cols="12" flat>
            <v-card flat>
              <v-list-item-content>
                {{
                $t('testAccountList.pageinfo')
                }}
              </v-list-item-content>
            </v-card>
          </v-col>
          <v-col class="col-12" v-if="errorStatus || successStatus">
            <v-alert
              type="error"
              v-if="errorStatus"
              class="alert-top text-left"
            >{{$t('testAccountList.errorMessage')}}</v-alert>
            <v-alert
              type="success"
              class="alert-top text-left"
              v-if="successStatus"
            >{{$t('testAccountList.successMessage')}}</v-alert>
          </v-col>
          <v-col cols="12" flat>
            <v-card flat>
              <v-list-item-content>
                {{
                $t('testAccountList.special_notes')
                }}
              </v-list-item-content>
              <TextArea
                v-model="testAccounts"
                :label="$t('testAccountList.special_notes')"
                type="text"
                outlined
                rows="10"
              />
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-item-group>
    <v-col cols="12">
      <v-card flat>
        <v-divider></v-divider>
        <v-card-actions class="mx-4">
          <v-spacer></v-spacer>

          <Button
            :disabled="testAccounts === ''"
            :loading="isLoading"
            class="white--text submit-account ml-6"
            depressed
            @click="submitTestAccount"
          >
            {{
            $t(
            'testAccountList.btnSaveChanges'
            )
            }}
          </Button>
        </v-card-actions>
      </v-card>
    </v-col>
  </v-card>
</template>
<script lang="ts">
import { Component, Vue, Watch, Prop } from 'vue-property-decorator';
import { Getter, namespace, Action } from 'vuex-class';
import Button from '@/Atomic/Button/Button.vue';
import TextArea from '@/Atomic/TextArea/TextArea.vue';

const TestAccountModule = namespace('TestAccountModule');

@Component({
  components: {
    Button,
    TextArea
  }
})
export default class TestAccount extends Vue {
  @Prop({ default: 0 })
  public id!: number;

  @TestAccountModule.Action('addTestAccounts')
  public addTestAccounts!: any;
  @TestAccountModule.Getter('isLoading')
  public isLoading!: boolean;
  @TestAccountModule.Getter('successStatus') public successStatus!: boolean;
  @TestAccountModule.Getter('errorStatus') public errorStatus!: boolean;
  @TestAccountModule.Action('clearStatus') public clearStatus!: any;

  private testAccounts: string = '';

  private submitTestAccount() {
    this.addTestAccounts({
      testAccounts: this.testAccounts
    });
  }

  private mounted() {
    this.clearStatus();
  }
}
</script>

<style lang="scss" scoped>
@import './../../assets/styles/theme.scss';
</style>
