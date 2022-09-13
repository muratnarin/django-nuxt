<template>
  <v-app-bar app dense clipped-right>
    <v-app-bar-nav-icon @click="$store.commit('setMini')"></v-app-bar-nav-icon>
    <v-spacer> </v-spacer>
    <v-btn
      v-for="locale in availableLocales"
      :key="locale.code"
      text
      plain
      @click="$i18n.setLocale(locale.code)"
      >{{ locale.code }}</v-btn
    >
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
            <v-list-item to="/">
              <v-list-item-icon class="mr-1">
                <v-icon small>mdi-view-dashboard</v-icon>
              </v-list-item-icon>
              <v-list-item-title>{{
                $t("button.frontPage")
              }}</v-list-item-title>
            </v-list-item>
            <v-list-item to="/admin/change-password-admin">
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
        </v-card>
      </v-menu>
    </template>
  </v-app-bar>
</template>

<script>
export default {
  name: "CHeader",
  data: () => ({
    menu: false,
  }),
  computed: {
    availableLocales() {
      return this.$i18n.locales.filter((i) => i.code !== this.$i18n.locale);
    },
  },
};
</script>
