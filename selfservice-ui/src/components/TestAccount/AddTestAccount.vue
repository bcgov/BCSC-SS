/** * Add TestAccount component */

<template>
  <v-card class="mx-auto " flat="">
    <v-item-group mandatory>
      <v-container>
        <v-row class="mx-4">
          <v-col cols="12" flat>
            <v-card flat>
              <div
                class="text-left"
                v-html="$t('AddTestAccount.pageinfo')"
              ></div>
            </v-card>
          </v-col>

          <v-col class="col-12" v-if="errorStatus || successStatus">
            <Alert
              type="error"
              v-if="errorStatus"
              class="alert-top text-left"
              >{{ $t('AddTestAccount.errorMessage') }}</Alert
            >
            <Alert
              type="success"
              class="alert-top text-left"
              v-if="successStatus"
            >
              {{ successCount.created }}
              {{ $t('AddTestAccount.successCreatedMessage') }}
              <br />
              {{ successCount.skipped }}
              {{ $t('AddTestAccount.successSkippedMessage') }}
            </Alert>
          </v-col>
          <v-col cols="12" flat>
            <v-card flat>
              <TextArea
                v-model="testAccounts"
                :label="$t('AddTestAccount.special_notes')"
                type="text"
                outlined
                rows="10"
                name="test-account-text"
                id="test-account-text"
                data-test-id="test-account-text"
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
            class="white--text submit-test-account ml-6"
            depressed
            @click="submitTestAccount"
            name="btn-test-account"
            data-test-id="btn-test-account"
            >{{ $t('AddTestAccount.btnSaveChanges') }}</Button
          >
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
import Alert from '@/Atomic/Alert/Alert.vue';

const TestAccountModule = namespace('TestAccountModule');

@Component({
  components: {
    Button,
    TextArea,
    Alert,
  },
})
export default class TestAccount extends Vue {
  @Prop({ default: 0 })
  public id!: number;

  @TestAccountModule.Action('addTestAccounts')
  public addTestAccounts!: any;
  @TestAccountModule.Getter('isLoading')
  public isLoading!: boolean;

  @TestAccountModule.Action('clearStatus') public clearStatus!: any;
  @TestAccountModule.Getter('getTestAccountSuccessData')
  public getTestAccountSuccessData!: any;

  private testAccounts: string = '';
  private successCount: any = { created: 0, skipped: 0 };
  private successStatus: boolean = false;
  private errorStatus: boolean = false;

  @Watch('getTestAccountSuccessData')
  private ongetTestAccountSuccessDataChanged(val: any) {
    const { successStatus, errorStatus, testAccountSuccessData } = val;
    this.clearAllStatus();
    if (successStatus) {
      this.successStatus = true;
      this.successCount = testAccountSuccessData;
    } else if (errorStatus) {
      this.errorStatus = true;
    }
    setTimeout(() => {
      this.clearAllStatus();
      this.clearStatus();
    }, 10000);
  }

  private submitTestAccount() {
    this.addTestAccounts({
      testAccounts: this.testAccounts,
    });
  }
  private clearAllStatus() {
    this.errorStatus = false;
    this.successStatus = false;
  }

  private mounted() {
    this.clearAllStatus();
    this.clearStatus();
  }
}
</script>

<style lang="scss" scoped>
@import './../../assets/styles/theme.scss';
</style>
