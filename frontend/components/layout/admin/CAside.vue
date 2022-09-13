<template>
  <v-navigation-drawer
    app
    permanent
    :expand-on-hover="mini"
    :mini-variant="mini"
    width="220"
  >
    <template #prepend>
      <v-row justify="center">
        <v-col class="d-flex justify-center">
          <v-img
            src="/logo-red.png"
            contain
            max-height="48"
            max-width="100"
            class="mr-5"
          ></v-img>
        </v-col>
      </v-row>
    </template>

    <v-divider></v-divider>
    <c-menu></c-menu>

    <!--    <template v-if="$auth.user" #append>-->
    <!--      <v-expansion-panels flat class="pa-1">-->
    <!--        <v-expansion-panel>-->
    <!--          <v-expansion-panel-header class="pa-0 pb-1 align-end">-->
    <!--            <div>-->
    <!--              <v-avatar class="mb-1">-->
    <!--                <img-->
    <!--                  v-if="$auth.user.avatar"-->
    <!--                  alt="Avatar"-->
    <!--                  :src="$auth.user.avatar"-->
    <!--                />-->
    <!--                <v-icon v-else>mdi-account</v-icon>-->
    <!--              </v-avatar>-->
    <!--              <div>-->
    <!--                <div class="text-h6">-->
    <!--                  {{ $auth.user.fullName }}-->
    <!--                </div>-->
    <!--                <div class="subtitle-2">{{ $auth.user.email }}</div>-->
    <!--              </div>-->
    <!--            </div>-->
    <!--            <template #actions>-->
    <!--              <v-icon class="mb-3"> $expand </v-icon>-->
    <!--            </template>-->
    <!--          </v-expansion-panel-header>-->
    <!--          <v-expansion-panel-content class="pa-0">-->
    <!--            <v-list dense>-->
    <!--              <v-list-item-->
    <!--                @click="-->
    <!--                  $auth.logout({-->
    <!--                    data: { refresh: $auth.strategy.refreshToken.get() },-->
    <!--                  })-->
    <!--                "-->
    <!--              >-->
    <!--                <v-list-item-content>-->
    <!--                  <v-list-item-title>{{-->
    <!--                    $t("button.logout")-->
    <!--                  }}</v-list-item-title>-->
    <!--                </v-list-item-content>-->
    <!--              </v-list-item>-->
    <!--            </v-list>-->
    <!--          </v-expansion-panel-content>-->
    <!--        </v-expansion-panel>-->
    <!--      </v-expansion-panels>-->
    <!--      <div @click="profile = !profile"></div>-->

    <!--      <v-expand-transition>-->
    <!--        <v-card-->
    <!--          v-if="profile"-->
    <!--          height="100"-->
    <!--          width="100"-->
    <!--          class="mx-auto secondary"-->
    <!--        ></v-card>-->
    <!--      </v-expand-transition>-->
    <!--    </template>-->
  </v-navigation-drawer>
</template>

<script>
import CMenu from "~/components/layout/admin/CMenu";
export default {
  name: "CAside",
  components: { CMenu },
  data: () => ({
    profile: false,
  }),
  computed: {
    mini: {
      get() {
        return this.$store.state.mini;
      },
      set() {
        this.$store.commit("setMini");
      },
    },
  },
};
</script>
