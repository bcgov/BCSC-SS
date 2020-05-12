/** * RemaingAccounts component */

<template>
  <div
    class="remaining-acc-txt"
    v-if="getTestAccountCount && getTestAccountCount.total"
  >
    <span class="count" :class="getTestAccountCount.warning && 'not-available'">
      {{ getTestAccountCount.available }}</span
    ><span class="divide">/</span
    ><span class="total">{{ getTestAccountCount.total }}</span>
    <span class="remaining-text">{{
      $t('dashboard.txtTestAccountRemain')
    }}</span>
  </div>
</template>
<script lang="ts">
import { Component, Vue, Watch, Prop } from 'vue-property-decorator';
import { Getter, namespace, Action } from 'vuex-class';

const TestAccountModule = namespace('TestAccountModule');

@Component
export default class RemaingAccounts extends Vue {
  @TestAccountModule.Getter('getTestAccountCount')
  public getTestAccountCount!: any;
  @TestAccountModule.Action('loadTestAccountCount')
  public loadTestAccountCount!: any;

  private mounted() {
    this.loadTestAccountCount();
  }
}
</script>

<style lang="scss" scoped>
@import './../../assets/styles/theme.scss';
.remaining-acc-txt {
  color: $BCgovFontColorInvertedDark;
  & .count {
    font-size: 48px;
    font-weight: bold;
    color: $succssGreen;
    &.not-available {
      color: $BCgovInputError;
    }
  }
  & .total {
    font-size: 36px;
    font-weight: bold;
  }
  & .divide {
    font-size: 36px;
    font-weight: bold;
    margin: 0 6px;
  }
  & .remaining-text {
    font-weight: bold;
    font-size: 22px;
    margin-left: 10px;
  }
}
</style>
