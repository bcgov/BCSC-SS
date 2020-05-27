/** ErrorPage component */

<template>
  <v-card class="errorpage" flat>
    <v-container>
      <v-row>
        <v-col cols="12" flat>
          <v-card flat>
            <div class="not-found" v-if="type !=='unauthorized'">{{$t('errorpage.404')}}</div>
            <div class="not-found-text">
              {{$t(
              type !=='unauthorized' ?
              'errorpage.pageNotFound' :
              'errorpage.unAuthorized'
              )}}
            </div>
          </v-card>
        </v-col>

        <v-col cols="12">
          <v-divider class="divide"></v-divider>
        </v-col>

        <v-col cols="12">
          <v-card flat class="return-text">
            <div>{{$t(type !=='unauthorized' ? 'errorpage.pageYouLooking':'errorpage.youAreNotAuthorized')}}</div>
            <div v-html="$t('errorpage.returnTo')"></div>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </v-card>
</template>
<script lang="ts">
import { Component, Vue, Watch, Prop } from 'vue-property-decorator';

@Component({
  components: {}
})
export default class ContactUs extends Vue {
  @Prop({ default: '404' })
  public type!: string;
}
</script>

<style lang="scss" scoped>
@import './../../assets/styles/theme.scss';
.errorpage {
  color: $BCgovFontColorInvertedDark !important;
  width: 100%;
  & .not-found {
    font-size: 48px;
    font-weight: bold;
    color: $BCgovFontColorInvertedDark;
  }
  & .not-found-text {
    font-weight: bold;
    font-size: 22px;
    margin-left: 10px;
    color: $BCgovFontColorInvertedDark;
  }
  & .return-text {
    font-size: 16px;
    color: $BCgovFontColorInvertedDark;

    & div {
      margin-top: 20px;
    }
  }
  & .divide {
    width: 100%;
  }
}
</style>
