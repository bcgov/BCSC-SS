/** * Input atomic component * Primary buttons allow users to carry out an
important action on your service, such as Download or Submit. */

<template>
  <v-text-field
    :value="value"
    :counter="counter"
    :label="label"
    :required="required"
    @input="input"
    @blur="input"
    v-bind="$attrs"
  ></v-text-field>
</template>

<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator';

/**
 *
 * @displayName  Input
 */

@Component
export default class Input extends Vue {
  /**
   * The counter for the input.
   *
   */
  @Prop({
    default: ''
  })
  private counter!: string | number;

  /**
   * The type for the input.
   * @values input, password
   */
  @Prop({
    default: 'text'
  })
  private type!: string;

  /**
   *  value for input
   */
  @Prop({
    default: ''
  })
  private value!: string;

  /**
   *  label text
   */
  @Prop({
    default: ''
  })
  private label!: string;

  /**
   *  required
   */
  @Prop({
    default: false
  })
  private required!: boolean;

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
</style>
