<template>
  <div>
    <v-card-title class="px-0"
      >{{ $t("label.blogs") }} <v-spacer></v-spacer>
      <v-pagination
        v-model="options.page"
        :length="Math.ceil(total / options.itemsPerPage)"
        :color="$vuetify.theme.dark ? 'grey' : 'primary'"
        @input="$fetch"
      ></v-pagination
    ></v-card-title>
    <v-card flat>
      <v-card-text class="pa-0">
        <v-row>
          <v-col v-for="item in items" :key="item.id" cols="12" lg="3">
            <f-blog-list-card :item="item"></f-blog-list-card>
          </v-col>
        </v-row>
      </v-card-text>
      <v-card-actions>
        <v-row justify="center">
          <v-col cols="12" md="6"> </v-col>
        </v-row>
      </v-card-actions>
    </v-card>
  </div>
</template>

<script>
import FBlogListCard from "~/components/blogs/FBlogListCard";
export default {
  name: "FBlogList",
  components: { FBlogListCard },
  data: () => ({
    items: [],
    total: [],
    options: {
      itemsPerPage: 12,
      page: 1,
    },
  }),
  async fetch() {
    const { total, result } = await this.$axios.$post("/api/getblogs/", {
      ...this.options,
    });
    this.items = result;
    this.total = total;
  },
  created() {},
  methods: {},
};
</script>
