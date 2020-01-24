/** * ListPackage component */

<template>
  <v-card class="mx-auto" style="max-width: 80%;">
    <v-toolbar flat class="bc-subtitle" dark>
      <v-btn icon @click="$router.push('/project/technical/' + projectId)" aria-label="Back Button">
        <v-icon>mdi-arrow-left</v-icon>
      </v-btn>
      <v-toolbar-title>Select Package</v-toolbar-title>
      <div class="flex-grow-1"></div>
      <v-col class="col-lg-4 col-md-5 col-8">
        <v-alert type="error" v-if="errorStatus" class="alert-top">Something went wrong...</v-alert>
      </v-col>
      <div class="flex-grow-1"></div>
    </v-toolbar>
    <v-divider></v-divider>
    <v-item-group mandatory :value="slectedPackage">
      <v-container>
        <v-row class="ma-5">
          <v-col cols="12" flat>
            <v-card flat>
              <v-list-item-content>Choosing a package level</v-list-item-content>
              <v-list-item-content>Package 1 - best fit for organizations looking for a digital signature</v-list-item-content>
              <v-list-item-content>Package 2 - best fit for organizations who want to know who the user is and communicate directly with their users electronically</v-list-item-content>
              <v-list-item-content>Package 3 - best fit for organizations who want to know who the user is and communicate directly with their users non-electronically</v-list-item-content>
            </v-card>
          </v-col>
          <v-col v-for="(packageData, idx) in getPackageList" :key="idx" cols="12" md="12">
            <v-item v-slot:default="{ active }" :value="packageData.id">
              <v-card
                class="d-flex align-center pa-4"
                :class="active ? 'active-bg' : ''"
                @click="selectedPackage(packageData.id)"
              >
                <v-list-item three-line>
                  <v-list-item-content>
                    <v-list-item-title class="headline mb-1">
                      {{
                      packageData.packageName
                      }}
                    </v-list-item-title>
                    <v-list-item-subtitle>
                      {{
                      packageData.description
                      }}
                    </v-list-item-subtitle>
                    <v-list-item-subtitle
                      v-for="claimName in packageData.claimNames"
                      :key="claimName"
                    >
                      <v-icon color="#969798" x-small>mdi-check-circle</v-icon>
                      {{ claimName }}
                    </v-list-item-subtitle>
                  </v-list-item-content>
                </v-list-item>
                <v-spacer></v-spacer>
                <div v-if="!active" class="text-center mr-5">
                  <v-icon color="#eae9e9" x-large>mdi-check-circle-outline</v-icon>
                  <!-- Select this package -->
                </div>
                <div v-if="active" class="display-3 flex-grow-1 text-center mr-5">
                  <v-icon color="green" x-large>mdi-check-circle</v-icon>
                </div>
                <!-- </v-scroll-y-transition> -->
              </v-card>
            </v-item>
          </v-col>
        </v-row>
      </v-container>
    </v-item-group>
    <v-col cols="12">
      <v-card flat class="ma-5">
        <v-divider></v-divider>
        <v-card-actions>
          <!-- <v-btn text @click="$refs.form.reset()">Clear</v-btn> -->
          <v-spacer></v-spacer>
          <Button
            :disabled="!slectedPackage"
            :loading="isLoading"
            class="white--text"
            color="indigo accent-4"
            depressed
            @click="submitPackage"
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
const PackageModule = namespace('PackageModule');

@Component({
  components: {
    Button
  }
})
export default class ListPackage extends Vue {
  @Prop({ default: 0 })
  public id!: number;
  @PackageModule.Getter('successStatus') public successStatus!: boolean;
  @PackageModule.Getter('errorStatus') public errorStatus!: boolean;
  @PackageModule.Action('loadPackage') public loadPackage!: any;
  @PackageModule.Getter('getPackageList') public getPackageList!: [];
  @PackageModule.Action('loadSinglePackage') public loadSinglePackage!: any;
  @PackageModule.Action('clearStatus') public clearStatus!: any;
  @PackageModule.Action('removePackage') public removePackage!: any;
  @PackageModule.Getter('getPackageMessage') public getPackageMessage!: any;

  private slectedPackage: number = 1;
  private isLoading: boolean = false;
  private projectId: number = this.id || 0;

  @Watch('successStatus')
  private onStatusChanged(val: any, oldVal: any) {
    setTimeout(this.clearStatus, 3000);
  }

  private remove(id: string) {
    const confrm = confirm('Are you sure to delete ?');
    if (confrm) {
      this.removePackage(id);
    }
  }
  private mounted() {
    this.loadPackage();
  }
  private selectedPackage(packageVal: number) {
    this.slectedPackage = packageVal;
  }
  private submitPackage() {
    // console.log('this.slectedPackage ', this.slectedPackage);
    // add package to project com ehere
  }
}
</script>
<style scoped>
.alert-top {
  margin-top: 17px;
}
</style>

<style lang="scss" scoped>
@import './../../assets/styles/theme.scss';
.active-bg {
  background-color: $BCgovActiveBg;
}
</style>
