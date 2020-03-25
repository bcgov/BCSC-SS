/** * ClientID component */

<template>
  <v-card class="mt-5" :class="getDataScopeClasses('scopePackageId')">
    <v-toolbar dense class="bc-subtitle-2" dark>
      <v-card-title>
        {{
        $t('summaryPage.packageTestTitle')
        }}
        <v-icon small class="ml-3" @click="$router.push(`/project/${id}/package`)">mdi-pencil</v-icon>
      </v-card-title>
    </v-toolbar>

    <v-list dense v-if="getPackageList.length > 0" class="px-5">
      <v-list-item>
        <v-list-item-content class="align-self-start pr-30">
          {{
          $t('summaryPage.labelDataPackageReqd')
          }}
          <span
            class="small-hint pad-50"
            v-html="$t('summaryPage.labelDataPackageReqdHint')"
          ></span>
        </v-list-item-content>
        <v-list-item-content class="align-end">
          <div v-if="selectedPackage.packageName !==''">
            <v-icon small class="mr-1">mdi-package-variant</v-icon>
            {{ selectedPackage.packageName }}
          </div>
          <div v-for="claimName in selectedPackage.claimNames" :key="claimName" class="ml-5">
            <v-icon color="#969798" x-small>mdi-check-circle</v-icon>
            {{ claimName }}
          </div>
        </v-list-item-content>
      </v-list-item>
    </v-list>
  </v-card>
</template>
<script lang="ts">
import { Component, Vue, Prop, Watch } from 'vue-property-decorator';
import { Getter, namespace, Action } from 'vuex-class';

import Loading from '@/Atomic/Loading/Loading.vue';

const PackageAndTestModule = namespace('PackageAndTestModule');

@Component({
  components: { Loading }
})
export default class ProjectInfoSummary extends Vue {
  @Prop({ default: 0 })
  public id!: number;
  @Prop({ default: {} })
  public technicalReq!: any;

  @Prop({ default: {} })
  public getDataScopeClasses!: any;

  @PackageAndTestModule.Action('loadPackage') public loadPackage!: any;
  @PackageAndTestModule.Getter('getPackageList') public getPackageList!: [];

  private selectedPackage: any = {
    claimNames: '',
    description: '',
    id: '',
    packageName: ''
  };

  @Watch('getPackageList')
  private ongetPackageListChanged() {
    if (
      this.technicalReq.scopePackageId &&
      this.technicalReq.scopePackageId !== null
    ) {
      this.selectedPackage = this.getSelectedPackage(
        this.technicalReq.scopePackageId
      );
    }
  }

  private getSelectedPackage(packageId: number) {
    const selectedPack = this.getPackageList.find(
      (packageData: any) => packageData.id === packageId
    );
    return selectedPack;
  }

  private created() {
    this.loadPackage();
  }
}
</script>

