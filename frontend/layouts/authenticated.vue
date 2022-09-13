<template>
  <v-app dark>
    <c-aside></c-aside>
    <c-header></c-header>
    <v-main>
      <v-container fluid>
        <c-toast></c-toast>
        <Nuxt />
      </v-container>
    </v-main>
    <v-navigation-drawer v-model="rightDrawer" :right="right" temporary fixed>
      <v-list>
        <v-list-item @click.native="right = !right">
          <v-list-item-action>
            <v-icon light> mdi-repeat </v-icon>
          </v-list-item-action>
          <v-list-item-title>Switch drawer (click me)</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
  </v-app>
</template>

<script>
import CToast from "~/components/common/cToast";
import CAside from "~/components/layout/admin/CAside";
import CHeader from "~/components/layout/admin/CHeader";
export default {
  name: "AuthenticatedLayout",
  components: { CHeader, CAside, CToast },
  middleware: ["isSuperUser"],
  data() {
    return {
      clipped: false,
      drawer: false,
      fixed: false,
      items: [
        {
          icon: "mdi-apps",
          title: "Welcome",
          to: "/",
        },
        {
          icon: "mdi-chart-bubble",
          title: "Inspire",
          to: "/inspire",
        },
      ],
      miniVariant: false,
      right: true,
      rightDrawer: false,
    };
  },
};
</script>
