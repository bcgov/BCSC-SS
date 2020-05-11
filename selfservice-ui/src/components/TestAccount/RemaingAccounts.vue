/** * RemaingAccounts component */

<template>
  <div
    class="text-center remaining-acc-txt"
    v-if="getTestAccountCount && getTestAccountCount.total"
  >
    <span class="count" :class="getTestAccountCount.warning && 'not-available'">
      {{ getTestAccountCount.available }}</span
    ><span class="divide">/</span
    ><span class="total">{{ getTestAccountCount.total }}</span>
    {{ $t('dashboard.txtTestAccountRemain') }}
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
    font-size: 24px;
    margin: 2px;
    font-weight: bold;
    color: $succssGreen;
    &.not-available {
      color: $BCgovInputError;
    }
  }
  & .total {
    margin: 2px;
    font-size: 20px;
    font-weight: bold;
  }
  & .divide {
    font-size: 20px;
    font-weight: bold;
  }
}
</style>
