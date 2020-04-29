<template>
  <v-card flat>
    <ContactUs />
  </v-card>
</template>

<script>
// @ is an alias to /src
import { Component, Vue } from 'vue-property-decorator';
import ContactUs from '@/components/ContactUs/ContactUs.vue';

@Component({
  components: {
    ContactUs
  }
})
// Home goes here
export default class ContactUsPage extends Vue {}
</script>
