/** * TestAccountRequest component */

<template>
  <v-card class="mx-auto outer-card">
    <v-toolbar flat class="bc-subtitle padding-0" dark>
      <v-btn icon @click="goBack()" :aria-label="$t('testAccount.btnBack')">
        <v-icon>mdi-arrow-left</v-icon>
      </v-btn>
      <h1 class="bc-h1-sub-ttile">{{ $t('testAccount.pagetitle') }}</h1>
      <div class="flex-grow-1"></div>
    </v-toolbar>
    <v-divider></v-divider>
    <v-item-group mandatory :value="slectedNumber">
      <v-container>
        <v-row class="mx-4">
          <v-col cols="12" class="pb-0" flat>
            <Alert type="error" v-if="errorStatus" class="alert-top">Something went wrong...</Alert>
            <v-card flat class="pb-0">
              <!-- <v-list-item-content>BCSC Test Account</v-list-item-content> -->
              <v-list-item-content v-html="$t('testAccount.pageinfo', { package: 'package' })"></v-list-item-content>
            </v-card>
          </v-col>

          <v-col cols="12" class="pt-0" flat>
            <v-card flat>
              <v-list-item-content>{{ $t('testAccount.how_many_test_account') }}</v-list-item-content>
            </v-card>
          </v-col>

          <v-col v-for="(testAccount, idx) in noOfTestAccounts" :key="idx" class="card-width">
            <v-item v-slot:default="{ active }" :value="testAccount" class="test-account">
              <v-card
                class="d-flex align-center pa-4 test-account"
                :class="active ? 'active-bg' : ''"
                @click="selectedTestAccount(testAccount)"
                @keyup.enter="selectedTestAccount(testAccount)"
                :data-test-id="`input-select-test-account-${testAccount}`"
              >
                <v-list-item>
                  <v-list-item-content class="text-center">
                    <v-list-item-title class="headline">{{ testAccount }}</v-list-item-title>
                    <v-list-item-subtitle></v-list-item-subtitle>
                  </v-list-item-content>
                </v-list-item>
                <v-spacer></v-spacer>
              </v-card>
            </v-item>
          </v-col>
          <v-col cols="12" flat>
            <v-card flat>
              <v-list-item-content>{{ $t('testAccount.special_notes') }}</v-list-item-content>
              <v-list-item-content class="subtitle-1" v-html="$t('testAccount.specialNotesInfo')"></v-list-item-content>
              <!-- <TextArea
                v-model="notes"
                :label="$t('testAccount.special_notes')"
                type="text"
                outlined
              />-->
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
            @click="goBack()"
            @keyup.enter="goBack()"
            :aria-label="$t('testAccount.btnBack')"
            secondary
            data-test-id="btn-cancel-test-account"
          >
            {{
            $t(
            showWizardExperience()
            ? 'testAccount.btnBack'
            : 'testAccount.btnCancel'
            )
            }}
          </Button>
          <Button
            :disabled="!slectedNumber"
            :loading="isLoading"
            class="white--text submit-account ml-6"
            depressed
            @click="submitTestAccount"
            @keyup.enter="submitTestAccount"
            data-test-id="btn-submit-test-account"
          >
            {{
            $t(
            showWizardExperience()
            ? 'testAccount.btnNext'
            : 'testAccount.btnSaveChanges'
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
import Alert from '@/Atomic/Alert/Alert.vue';

const PackageAndTestModule = namespace('PackageAndTestModule');
const TechnicalReqModule = namespace('TechnicalReqModule');
const SharedModule = namespace('SharedModule');

@Component({
  components: {
    Button,
    TextArea,
    Alert
  }
})
export default class TestAccountRequest extends Vue {
  @Prop({ default: 0 })
  public id!: number;
  @PackageAndTestModule.Getter('successStatus') public successStatus!: boolean;
  @PackageAndTestModule.Getter('errorStatus') public errorStatus!: boolean;
  @PackageAndTestModule.Action('loadPackage') public loadPackage!: any;
  @PackageAndTestModule.Getter('getPackageList') public getPackageList!: [];
  @PackageAndTestModule.Action('clearStatus') public clearStatus!: any;
  @PackageAndTestModule.Action('addTestAccountRequestToProject')
  public addTestAccountRequestToProject!: any;

  @TechnicalReqModule.Action('loadTechnicalReqDetails')
  public loadTechnicalReqDetails!: any;
  @TechnicalReqModule.Getter('getTechnicalReq')
  public getTechnicalReq!: any;
  @TechnicalReqModule.Getter('isLoading') public isLoading!: boolean;

  @SharedModule.Action('redirectFromSummaryPage')
  public redirectFromSummaryPage!: any;
  @SharedModule.Getter('isRedirectFromSummaryPage')
  public isRedirectFromSummaryPage!: boolean;

  private noOfTestAccounts: any = [1, 2, 3, 5];
  private notes: string = '';

  private slectedNumber: number = 1;
  // private isLoading: boolean = false;
  private projectId: number = this.id || 0;

  @Watch('successStatus')
  private onStatusChanged(val: any, oldVal: any) {
    setTimeout(this.clearStatus, 3000);
  }
  @Watch('getTechnicalReq')
  private ongetTechnicalReqChanged(val: any) {
    this.slectedNumber = val.noOfTestAccount || this.slectedNumber;
    this.notes = val.noteTestAccount || this.notes;
  }

  private selectedTestAccount(packageVal: number) {
    this.slectedNumber = packageVal;
  }
  private submitTestAccount() {
    // add package to project com ehere
    this.addTestAccountRequestToProject({
      noOfTestAccount: this.slectedNumber,
      noteTestAccount: this.notes,
      projectId: this.projectId
    });
  }

  private mounted() {
    if (this.id !== 0) {
      // this.isEditMode = true;
      this.loadTechnicalReqDetails(this.id);
    }
  }

  private goBack() {
    const redirectPage = this.showWizardExperience()
      ? `/project/${this.projectId}/package/`
      : `/project-container/${this.projectId}/`;

    this.redirectFromSummaryPage(false);
    this.$router.push(redirectPage);
  }
  private showWizardExperience() {
    if (this.isRedirectFromSummaryPage) {
      return false;
    }
    return true;
  }
}
</script>

<style lang="scss" scoped>
@import './../../assets/styles/theme.scss';
.active-bg {
  background-color: $BCgovActiveBg;
}
.card-width {
  max-width: 110px;
}
.text-center {
  text-align: center !important;
}
</style>
