/** * Select atomic component * Select allow users to carry out an important
action on your service, such as Download or Submit. */

<template>
  <!-- <v-Select :value="value" @input="input" v-bind="$attrs"></v-Select> -->

  <div class="bc-form-text">
    <div class="text-left my-1">{{label}}</div>
    <div
      class="text-left mb-1 subtitle-2 bc-help-text"
      v-if="helpText !==''"
      :class="helpClass"
    >{{helpText}}</div>

    <v-select :items="items" v-bind="$attrs" :label="label" @change="input" @input="input" solo></v-select>
  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator';

/**
 *
 * @displayName  Input
 */

@Component
export default class Select extends Vue {
  /**
   *  value for input
   */
  @Prop({
    default: ''
  })
  private items!: any;

  /**
   *  label text
   */
  @Prop({
    default: ''
  })
  private label!: string;

  /**
   *  helpText text
   */
  @Prop({
    default: ''
  })
  private helpText!: string;

  /**
   *  helpText class
   */
  @Prop({
    default: ''
  })
  private helpClass!: string;

  /**
   * input
   * @description update value on key up or blur
   * @param {string} inputval
   */
  private input(inputval: string) {
    this.$emit('input', inputval);
  }
}
</script>

<style lang="scss" scoped>
// @import './../../assets/styles/theme.scss';
.v-list-item__content {
  text-align: left;
}
</style>
