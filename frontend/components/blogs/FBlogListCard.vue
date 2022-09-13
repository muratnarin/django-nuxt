<template>
  <v-card height="350" rounded class="d-flex flex-column">
    <v-img
      class="white--text align-start"
      :src="item.image ? item.image : 'https://picsum.photos/id/1016/320/200'"
      max-height="150"
    >
    </v-img>
    <div class="flex-grow-1 overflow-auto mt-4">
      <div class="text-truncate px-4 font-weight-medium body-1">
        {{ item[$localize("title")] }}
      </div>

      <v-card-subtitle class="py-1 px-4 d-flex align-center text--disabled">
        <v-icon small class="mr-1">mdi-calendar</v-icon>
        {{ formatDate(item.created_at) }}
      </v-card-subtitle>
      <v-divider></v-divider>
      <v-card-text>
        <v-clamp autoresize :max-lines="3">
          {{ item[$localize("summary")] }}
        </v-clamp>
      </v-card-text>
    </div>

    <v-divider></v-divider>

    <v-card-actions class="py-1">
      <!--      <v-card-subtitle class="px-1 py-1 d-flex align-center font-italic">-->
      <!--        <v-icon small>mdi-account-edit-outline</v-icon>-->
      <!--        {{ item.operation_user || "Test user" }}-->
      <!--      </v-card-subtitle>-->
      <v-spacer></v-spacer>
      <v-btn color="indigo" text small :to="`/blogs/${item.slug}`">
        {{ $t("button.readMore") }}
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
import VClamp from "vue-clamp";
export default {
  name: "FBlogListCard",
  components: {
    VClamp,
  },
  props: {
    item: {
      type: Object,
      default: () => ({}),
    },
  },
  methods: {
    formatDate(date) {
      return this.$dt
        .fromISO(date)
        .setLocale(this.$i18n.locale)
        .toLocaleString(this.$dt.DATE_MED);
    },
  },
};
</script>
