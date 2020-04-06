<template>
  <v-container fluid>
    <v-row>
      <v-col cols="12">
        <h1 class="text-center main-headline">{{ $t('home.txtMainTitle') }}</h1>
      </v-col>
      <v-col cols="12" md="6" class="home-img"></v-col>
      <v-col cols="12" md="6" class="text-left">
        <v-card flat>
          <h2 class="second-headline">
            {{ $t('home.txtFitForOrganization') }}
          </h2>
          <div
            v-html="$t('home.txtsubcontent1')"
            class="second-sub-content"
          ></div>
          <div
            v-html="$t('home.txtsubcontent2')"
            class="second-sub-content"
          ></div>
          <div
            v-html="$t('home.txtsubcontent3')"
            class="second-sub-content"
          ></div>

          <h3 class="third-h3">{{ $t('home.txtsubTitle2') }}</h3>
          <div v-html="$t('home.txtsubcontent4')" class="subcontent3"></div>
          <v-card-actions class="btn-actions">
            <Button
              class="btn-all"
              color="#fcba19 !important"
              @click="$router.push('/help')"
              >{{ $t('home.btnLearmore') }}</Button
            >
            <Button
              class="btn-all getting-start-btn"
              @click="$router.push('/dashboard/')"
            >
              {{ $t('home.txtgetStarted') }}
            </Button>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator';
import Button from '@/Atomic/Button/Button.vue';

@Component({ components: { Button } })
export default class HelloWorld extends Vue {}
</script>

<style lang="scss" scoped>
@import './../../assets/styles/theme.scss';
.main-headline {
  font-size: 38px;
  font-weight: bold;
  color: $BCgovBlue5;
}
.second-headline {
  color: $BCgovGold5;
  font-size: 34px;
  margin-top: 28px;
}
.second-sub-content {
  color: $gray10;
  margin-top: 27px;
  font-size: 24px;
}
.third-h3 {
  font-size: 24px;
  font-weight: bold;
  color: $BCgovBlue5;
  margin-top: 65px;
}
.subcontent3 {
  width: 100%;
  margin-top: 25px;
  font-size: 20px;
  color: $gray10;

  // @include md {
  //   width: 80%;
  // }
  @include lg {
    width: 90%;
  }
  @include xl {
    width: 75%;
  }
}
.home-img {
  background-position: center;
  background-image: url('/img/login_with_mobile_card.png');
  @include lg {
    background-image: url('/img/login_with_mobile_card-500.png');
  }
  @include xl {
    background-image: url('/img/login_with_mobile_card-640.png');
  }
  min-height: 250px;
}
.btn-all {
  font-size: 22px;
}
.getting-start-btn {
  margin-left: 30px !important;
}
.btn-actions {
  margin-top: 50px;
}
</style>
