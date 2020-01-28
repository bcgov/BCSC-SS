/** * TestAccountRequest component */

<template>
  <v-card class="mx-auto" style="max-width: 80%;">
    <v-toolbar flat class="bc-subtitle" dark>
      <v-btn icon @click="$router.push('/project/package/' + projectId)" aria-label="Back Button">
        <v-icon>mdi-arrow-left</v-icon>
      </v-btn>
      <v-toolbar-title>Test Accounts</v-toolbar-title>
      <div class="flex-grow-1"></div>
      <v-col class="col-lg-4 col-md-5 col-8">
        <v-alert type="error" v-if="errorStatus" class="alert-top">Something went wrong...</v-alert>
      </v-col>
      <div class="flex-grow-1"></div>
    </v-toolbar>
    <v-divider></v-divider>
    <v-item-group mandatory :value="slectedNumber">
      <v-container>
        <v-row class="ma-5">
          <v-col cols="12" flat>
            <v-card flat>
              <!-- <v-list-item-content>BCSC Test Account</v-list-item-content> -->
              <v-list-item-content>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.</v-list-item-content>
            </v-card>
          </v-col>

          <v-col cols="12" flat>
            <v-card flat>
              <v-list-item-content>How many test accounts do you require?</v-list-item-content>
            </v-card>
          </v-col>

          <v-col v-for="(testAccount, idx) in noOfTestAccounts" :key="idx" class="card-width">
            <v-item v-slot:default="{ active }" :value="testAccount" class="select-package">
              <v-card
                class="d-flex align-center pa-4 select-package"
                :class="active ? 'active-bg' : ''"
                @click="selectedTestAccount(testAccount)"
              >
                <v-list-item>
                  <v-list-item-content class="text-center">
                    <v-list-item-title class="headline">{{testAccount}}</v-list-item-title>
                    <v-list-item-subtitle></v-list-item-subtitle>
                  </v-list-item-content>
                </v-list-item>
                <v-spacer></v-spacer>
                <!-- <div v-if="!active" class="text-center mr-5"> -->
                <!-- <v-icon color="#eae9e9" x-large>mdi-check-circle-outline</v-icon> -->
                <!-- Select this package -->
                <!-- </div>
                <div v-if="active" class="display-3 flex-grow-1 text-center mr-5">-->
                <!-- <v-icon color="green" x-large>mdi-check-circle</v-icon> -->
                <!-- </div> -->
                <!-- </v-scroll-y-transition> -->
              </v-card>
            </v-item>
          </v-col>
          <v-col cols="12" flat>
            <v-card flat>
              <v-list-item-content>Special requests or notes for test account creation</v-list-item-content>
              <TextArea
                v-model="notes"
                label="Special requests or notes for test account creation"
                type="text"
                outline
              />
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-item-group>
    <v-col cols="12">
      <v-card flat class="ma-5">
        <v-divider></v-divider>
        <v-card-actions>
          <v-spacer></v-spacer>
          <Button
            @click="$router.push('/project/package/' + projectId)"
            aria-label="Back Button"
            secondary
          >Go Back</Button>
          <Button
            :disabled="!slectedNumber"
            :loading="isLoading"
            class="white--text submit-package"
            depressed
            @click="submitTestAccount"
          >Next</Button>
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
const PackageAndTestModule = namespace('PackageAndTestModule');

@Component({
  components: {
    Button,
    TextArea
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

  private noOfTestAccounts: any = [1, 2, 3, 5];
  private notes: string = '';

  private slectedNumber: number = 1;
  private isLoading: boolean = false;
  private projectId: number = this.id || 0;

  @Watch('successStatus')
  private onStatusChanged(val: any, oldVal: any) {
    setTimeout(this.clearStatus, 3000);
  }

  // private mounted() {
  //   this.loadPackage();
  // }
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
