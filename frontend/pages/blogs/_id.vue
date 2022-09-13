<template>
  <v-container class="py-16">
    <v-row v-if="!$fetchState.pending" no-gutters>
      <v-col cols="12">
        <v-btn
          text
          plain
          left
          to="/blogs"
          class="text-capitalize px-0 py-1 mb-3"
        >
          <v-icon>mdi-arrow-left</v-icon>
          <div class="text-h6">{{ $t("label.blogs") }}</div>
        </v-btn>
      </v-col>
      <v-col cols="12">
        <f-blog-detail :item="item"></f-blog-detail>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { detailMixin } from "~/mixins/detailMixin";
import FBlogDetail from "~/components/blogs/FBlogDetail";

export default {
  name: "Id",
  components: { FBlogDetail },
  mixins: [detailMixin],
  layout: "guest",
  auth: false,
  data: () => ({
    itemName: "users",
    item: {},
  }),
  async fetch() {
    const { id } = this.$route.params;
    try {
      this.item = await this.$axios.$post("/api/getblogbyid/", { slug: id });
    } catch (e) {
      this.$handleError(e);
    }
  },
};
</script>
