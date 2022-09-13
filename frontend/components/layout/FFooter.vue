<template>
  <v-footer dark padless>
    <v-card
      flat
      tile
      class="indigo lighten-1 white--text text-center"
      width="100%"
    >
      <v-card-text>
        <v-btn
          v-for="(link, i) in social"
          :key="'icon' + i"
          class="mx-4 white--text"
          icon
          :href="'https://' + contact[link.code]"
          target="_blank"
        >
          <v-icon size="24px">
            {{ link.icon }}
          </v-icon>
        </v-btn>
      </v-card-text>

      <v-card-text class="white--text pt-0">
        <v-btn
          v-for="(link, i) in links"
          :key="'link' + i"
          color="white"
          text
          rounded
          class="my-2"
          :to="link.url"
        >
          {{ $t(`label.${link.text}`) }}
        </v-btn>
      </v-card-text>
      <v-card-text class="white--text pt-0">
        <v-btn
          small
          text
          rounded
          class="my-2 text-capitalize"
          @click="openDialog(1)"
          >{{ $t(`label.cookiePolicy`) }}</v-btn
        >
        <v-btn
          small
          text
          rounded
          class="my-2 text-capitalize"
          @click="openDialog(2)"
          >{{ $t(`label.clarificationText`) }}</v-btn
        >
      </v-card-text>

      <v-divider></v-divider>

      <v-card-text class="white--text d-flex justify-center">
        <v-img
          src="/logo-white.png"
          contain
          max-height="48"
          max-width="110"
        ></v-img>
      </v-card-text>
    </v-card>
    <v-dialog :key="dialogKey" v-model="dialog" width="800">
      <v-card>
        <v-toolbar class="mb-5">
          <v-toolbar-title>
            {{ dialogTitle }}
          </v-toolbar-title>
        </v-toolbar>
        <v-card-text>
          {{ dialogText }}
        </v-card-text>
      </v-card>
    </v-dialog>
  </v-footer>
</template>
<script>
export default {
  name: "FFooter",
  data: () => ({
    links: [
      {
        text: "home",
        url: "/",
      },
      {
        text: "schools",
        url: "/schools",
      },
      {
        text: "blogs",
        url: "/blogs",
      },
      {
        text: "announcements",
        url: "/announcements",
      },
      {
        text: "contactUs",
        url: "/contact-us",
      },
    ],
    social: [
      {
        icon: "mdi-facebook",
        code: "facebook",
      },
      {
        icon: "mdi-twitter",
        code: "twitter",
      },
      {
        icon: "mdi-instagram",
        code: "instagram",
      },
      {
        icon: "mdi-youtube",
        code: "youtube",
      },
    ],
    dialog: false,
    dialogKey: 0,
    dialogTitle: "",
    dialogText: "",
    contact: {},
  }),
  async fetch() {
    try {
      const { result } = await this.$axios.$post("/api/getcontacts/");
      this.contact = result[0] || {};
    } catch (e) {
      this.$handleError(e);
    }
  },
  methods: {
    openDialog(type) {
      this.dialogKey++;
      this.dialogText =
        type === 1
          ? this.$store.state.defaults.cookie_policy
          : this.$store.state.defaults.privacy_policy;
      this.dialogTitle =
        type === 1
          ? this.$t("label.cookiePolicy")
          : this.$t(`label.clarificationText`);
      this.dialog = true;
    },
  },
};
</script>
