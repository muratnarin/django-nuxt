<template>
  <v-list dense nav>
    <template v-for="item in menuItems">
      <v-list-item
        v-if="!item.subMenus"
        :key="item.title"
        link
        dense
        :to="item.url ? item.url : null"
        :disabled="!item.url"
        :title="item.title"
      >
        <v-list-item-icon class="mr-3">
          <v-icon>{{ item.icon }}</v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title>{{ $t(`label.${item.title}`) }}</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
      <v-list-group
        v-else
        :key="item.title"
        :color="$vuetify.theme.dark ? 'grey' : 'primary'"
        :group="`/${item.title.toLowerCase()}/*`"
      >
        <template #activator>
          <v-list-item-icon class="mr-3">
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-icon>
          <v-list-item-title>{{ $t(`label.${item.title}`) }}</v-list-item-title>
        </template>
        <v-list-item
          v-for="subItem in item.subMenus"
          :key="subItem.title"
          link
          :to="subItem.url ? subItem.url : null"
        >
          <v-list-item-icon class="mr-3" :class="isMini ? 'ml-1' : 'ml-2'">
            <v-icon :small="isMini">{{ subItem.icon }}</v-icon>
          </v-list-item-icon>
          <v-list-item-title>{{
            $t(`label.${subItem.title}`)
          }}</v-list-item-title>
        </v-list-item>
      </v-list-group>
    </template>
  </v-list>
</template>

<script>
export default {
  data: () => ({
    menuItems: [
      {
        title: "users",
        icon: "mdi-account-multiple",
        url: "/admin/users",
      },
      {
        title: "schools",
        icon: "mdi-school",
        url: "/admin/schools",
      },
      {
        title: "blogs",
        icon: "mdi-post",
        url: "/admin/blogs",
      },
      {
        title: "announcements",
        icon: "mdi-bullhorn",
        url: "/admin/announcements",
      },
      {
        title: "exchange",
        icon: "mdi-book-education",
        url: "/admin/exchange-programs",
      },
      {
        title: "settings",
        icon: "mdi-cogs",
        subMenus: [
          {
            title: "banners",
            icon: "mdi-image",
            url: "/admin/settings/banners",
          },
          {
            title: "contacts",
            icon: "mdi-map-marker-multiple",
            url: "/admin/settings/contacts",
          },
        ],
      },
    ],
  }),
  computed: {
    isMini() {
      return this.$store.state.mini;
    },
  },
};
</script>
