/** * Button atomic component * Primary buttons allow users to carry out an
important action on your service, such as Download or Submit. */

<template>
  <v-btn
    class="btn"
    :type="type"
    :name="name"
    v-bind:class="[
      secondary !== false ? 'secondary-btn' : 'primary',
      dark !== false ? 'dark-calss' : 'normal',
      disabled !== false ? 'disabled' : '',
    
    ]"
    :aria-disabled="disabled"
    :disabled="disabled"
    @click="click"
    v-bind="$attrs"
    :color="color !== '' ? color : undefined"
  >
    <!-- color="#fcba19 !important" -->
    <!-- yellowBtn !== false ? 'yellow-btn':'' -->
    <!-- @slot  Button display name-->
    <slot></slot>
  </v-btn>
</template>

<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator';

/**
 * All variation of button
 * @displayName  Buttons
 */

@Component
export default class Button extends Vue {
  /**
   * The name for the button.
   * @values button, submit
   */
  @Prop({
    default: 'button'
  })
  private name!: string;

  /**
   * The type for the button.
   */
  @Prop({
    default: 'button'
  })
  private type!: string;

  /**
   *  Dark Background  button.
   */
  @Prop({
    default: false
  })
  private dark!: boolean;

  /**
   *  Dark secondary  button. default will be primary
   */
  @Prop({
    default: false
  })
  private secondary!: boolean;

  /**
   *  Dark disabled  button.
   */
  @Prop({
    default: false
  })
  private disabled!: boolean;
  /**
   *  custom color button. default will be primary
   */
  @Prop({
    default: ''
  })
  private color!: string;

  /**
   * on click
   * @description update on click
   *
   */
  private click() {
    this.$emit('click');
  }
}
</script>

<style lang="scss" scoped>
@import './../../assets/styles/theme.scss';

.btn {
  border: none;
  padding: 10px 32px !important;
  min-height: 45px;
  display: block;
  text-align: center;
  text-decoration: none;
  font-size: 18px;
  font-weight: 700;
  letter-spacing: 1px;
  font-family: 'BCSans', 'Noto Sans', Verdana, Arial, sans-serif;
  cursor: pointer;
}

.btn:focus:not(.disabled) {
  outline: 4px solid #3b99fc;
  outline-offset: 1px;
}
.bc-btn:active:not(.disabled) {
  opacity: 1;
}
.secondary-btn {
  background: none !important;
  border: 2px solid $BCgovBlue5;
  color: $BCgovBlue5 !important;
  font-weight: 700;
}
.secondary-btn:hover:hover:not(.disabled) {
  opacity: 0.8;
  text-decoration: underline;
}
.secondary-btn:focus:hover:not(.disabled) {
  outline-offset: 1px;
  outline: 4px solid $BCgovABlue2;
}
.secondary-btn.normal:hover:hover:not(.disabled) {
  background-color: $BCgovBlue5 !important;
  color: $BCgovFontColorInverted !important;
}
.secondary-btn.dark-calss {
  background-color: $BCgovBlue5 !important;
  border: 2px solid $BCgovFontColorInverted;
  color: $BCgovFontColorInverted !important;
}

.secondary-btn.dark-calss:hover:hover:not(.disabled) {
  text-decoration: underline;
  background-color: $BCgovFontColorInverted !important;
  color: $BCgovFontColorInvertedDark !important;
  opacity: 1;
}

.primary {
  border: none;
  // background-color: #003366;
  border-radius: 4px;
  color: white;
  text-decoration: none;
}

.primary.normal {
  background-color: $BCgovBlue5 !important;
  color: white !important;
}
.primary.dark-calss {
  background-color: $BCgovFontColorInverted !important;
  color: $BCgovFontColorInvertedDark !important;
}
.primary.normal:hover:not(.disabled) {
  opacity: 0.8;
}

.dark-calss:hover:not(.disabled) {
  background-color: #f2f2f2;
  text-decoration: underline;
}
.dark-calss:active {
  background-color: $BCgovFontColorInverted !important;
}
.background-colour {
  background-color: $BCgovBlue5;
  height: 100px;
  width: 300px;
  display: flex;
  align-items: center;
  justify-content: center;
}
.disabled {
  cursor: not-allowed;
  opacity: 0.3;
}
.secondary-btn.theme--light.v-btn.v-btn--disabled:not(.v-btn--flat):not(.v-btn--text):not(.v-btn--outlined) {
  background-color: $BCgovFontColorInverted !important;
}
.primary.theme--light.v-btn.v-btn--disabled:not(.v-btn--flat):not(.v-btn--text):not(.v-btn--outlined) {
  background-color: $BCgovBlue5 !important;
}
</style>
