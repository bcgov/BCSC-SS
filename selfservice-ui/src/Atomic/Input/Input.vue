/** * Input atomic component * Primary buttons allow users to carry out an
important action on your service, such as Download or Submit. */

<template>
  <div class="bc-form-text">
    <div class="text-left my-1">
      {{ label }} <span v-if="optional" class="optional">*optional</span>
    </div>
    <div class="text-left mb-1 subtitle-2 bc-help-text" v-if="helpText !== ''">
      {{ helpText }}
    </div>
    <v-text-field
      :value="value"
      :counter="counter"
      :required="required"
      @input="input"
      v-bind="$attrs"
      @blur="$emit('blur')"
      class="input"
      :outlined="outlined"
      solo
    ></v-text-field>
  </div>
  <!-- outlined -->
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
    default: false,
  })
  private counter!: boolean | string | number;

  /**
   * The type for the input.
   * @values input, password
   */
  @Prop({
    default: 'text',
  })
  private type!: string;

  /**
   *  value for input
   */
  @Prop({
    default: '',
  })
  private value!: string;

  /**
   *  label text
   */
  @Prop({
    default: '',
  })
  private label!: string;

  /**
   *  required
   */
  @Prop({
    default: false,
  })
  private required!: boolean;
  /**
   *  outlined
   */
  @Prop({
    default: true,
  })
  private outlined!: boolean;
  /**
   *  helpText text
   */
  @Prop({
    default: '',
  })
  private helpText!: string;
  /**
   *  optional text
   */
  @Prop({
    default: false,
  })
  private optional!: boolean;

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
@import './../../assets/styles/theme.scss';

.v-application .primary--text {
  color: $BCgovBlue5 !important;
  caret-color: $BCgovBlue5 !important;
}
.optional {
  color: $BCgovABlue2;
  font-size: 14px;
  margin-left: 10px;
}
.bc-form-text {
  width: 100%;
}
</style>
