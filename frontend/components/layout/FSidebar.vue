<template>
  <v-navigation-drawer :value="drawer" temporary app @input="setDrawer">
    <v-list dense>
      <v-list-item v-for="item in items" :key="item.title" link :to="item.to">
        <v-list-item-icon class="mr-2">
          <v-icon>{{ item.icon }}</v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title>{{ $t(`label.${item.title}`) }}</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    </v-list>
    <template #append>
      <template v-if="$auth.user">
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
            <v-list-item-title>{{ $t("button.adminPanel") }}</v-list-item-title>
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
            <v-list-item-title>{{ $t("button.logout") }}</v-list-item-title>
          </v-list-item>
        </v-list>
      </template>
      <template v-else>
        <v-list dense>
          <v-list-item to="/auth/login">
            <v-list-item-title>{{
              $t("button.login").toLocaleUpperCase()
            }}</v-list-item-title>
          </v-list-item>
          <v-list-item to="/auth/register">
            <v-list-item-title>{{
              $t("button.register").toLocaleUpperCase()
            }}</v-list-item-title>
          </v-list-item>
        </v-list>
      </template>
    </template>
  </v-navigation-drawer>
</template>

<script>
export default {
  name: "FSidebar",
  data: () => ({
    items: [
      {
        icon: "mdi-school",
        title: "schools",
        to: "/schools",
      },
      {
        icon: "mdi-post-outline",
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

<style scoped></style>
