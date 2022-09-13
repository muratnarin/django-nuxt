<template>
  <v-app-bar
    app
    dense
    :color="$store.state.menuStyle.color"
    :dark="$store.state.menuStyle.dark"
    :flat="$store.state.menuStyle.flat"
  >
    <v-container class="fill-height pa-0">
      <nuxt-link to="/">
        <!--        :src="
        $store.state.menuStyle.dark ? '/logo-white.png' : '/logo-red.png'
        "-->
        <v-img
          src="/logo-red.png"
          contain
          max-height="48"
          max-width="100"
          class="mr-5"
        ></v-img>
      </nuxt-link>
      <template v-if="$vuetify.breakpoint.mdAndDown">
        <v-app-bar-nav-icon
          @click="$store.commit('setDrawer', true)"
        ></v-app-bar-nav-icon>
      </template>
      <template v-else>
        <v-btn v-for="item in items" :key="item.title" :to="item.to" text>{{
          $t(`label.${item.title}`)
        }}</v-btn>
      </template>

      <v-spacer> </v-spacer>
      <v-btn
        v-for="locale in availableLocales"
        :key="locale.code"
        text
        plain
        @click="$i18n.setLocale(locale.code)"
        >{{ locale.code }}</v-btn
      >
      <template v-if="$vuetify.breakpoint.lgAndUp">
        <template v-if="$auth.user">
          <v-menu v-model="menu" offset-y>
            <template #activator="{ on, attrs }">
              <v-btn text plain v-bind="attrs" v-on="on">
                {{ $t("label.myAccount") }}
              </v-btn>
            </template>

            <v-card>
              <v-list>
                <v-list-item>
                  <!--                <v-list-item-avatar>-->
                  <!--                  <img-->
                  <!--                    src="https://cdn.vuetifyjs.com/images/john.jpg"-->
                  <!--                    alt="John"-->
                  <!--                  />-->
                  <!--                </v-list-item-avatar>-->

                  <v-list-item-content>
                    <v-list-item-title>{{
                      $auth.user.first_name + " " + $auth.user.last_name
                    }}</v-list-item-title>
                    <v-list-item-subtitle>{{
                      $auth.user.email
                    }}</v-list-item-subtitle>
                  </v-list-item-content>
                </v-list-item>
              </v-list>

              <v-divider></v-divider>

              <v-list dense>
                <v-list-item v-if="$auth.user.is_superuser" to="/admin/users">
                  <v-list-item-icon class="mr-1">
                    <v-icon small>mdi-view-dashboard</v-icon>
                  </v-list-item-icon>
                  <v-list-item-title>{{
                    $t("button.adminPanel")
                  }}</v-list-item-title>
                </v-list-item>
                <v-list-item to="/auth/change-password">
                  <v-list-item-icon class="mr-1">
                    <v-icon small>mdi-lock</v-icon>
                  </v-list-item-icon>
                  <v-list-item-title>{{
                    $t("button.changePassword")
                  }}</v-list-item-title>
                </v-list-item>
                <v-list-item
                  @click="
                    $auth.logout({
                      data: { refresh: $auth.strategy.refreshToken.get() },
                    })
                  "
                >
                  <v-list-item-icon class="mr-1">
                    <v-icon small>mdi-logout</v-icon>
                  </v-list-item-icon>
                  <v-list-item-title>{{
                    $t("button.logout")
                  }}</v-list-item-title>
                </v-list-item>
              </v-list>
            </v-card>
          </v-menu>
        </template>
        <template v-else>
          <v-btn text plain small to="/auth/register">{{
            $t("button.register")
          }}</v-btn>
          <v-btn text plain small to="/auth/login">{{
            $t("button.login")
          }}</v-btn>
        </template>
      </template>
    </v-container>
  </v-app-bar>
</template>

<script>
export default {
  name: "FHeader",
  data: () => ({
    lang: 1,
    menu: false,
    items: [
      {
        icon: "mdi-school",
        title: "schools",
        to: "/schools",
      },
      {
        icon: "mdi-blogger",
        title: "blogs",
        to: "/blogs",
      },
      {
        icon: "mdi-bell",
        title: "announcements",
        to: "/announcements",
      },
      {
        icon: "mdi-email-outline",
        title: "contactUs",
        to: "/contact-us",
      },
    ],
  }),
  computed: {
    availableLocales() {
      return this.$i18n.locales.filter((i) => i.code !== this.$i18n.locale);
    },
    drawer() {
      return this.$store.state.drawer;
    },
  },
  methods: {
    setDrawer(val) {
      this.$store.commit("setDrawer", val);
    },
  },
};
</script>
