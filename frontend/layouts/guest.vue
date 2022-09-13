<template>
  <v-app dark>
    <f-header></f-header>
    <f-sidebar></f-sidebar>
    <v-main class="pt-0">
      <c-toast></c-toast>
      <Nuxt />
    </v-main>
    <f-footer></f-footer>
  </v-app>
</template>

<script>
import CToast from "~/components/common/cToast";
import FHeader from "~/components/layout/FHeader";
import FFooter from "~/components/layout/FFooter";
import FSidebar from "~/components/layout/FSidebar";
export default {
  name: "GuestLayout",
  components: { FFooter, FHeader, CToast, FSidebar },
};
</script>
