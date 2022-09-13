<template>
  <v-container :fluid="$vuetify.breakpoint.mdAndDown" class="pt-16">
    <v-row>
      <v-col><f-blog-list></f-blog-list> </v-col>
    </v-row>
  </v-container>
</template>

<script>
import FBlogList from "~/components/blogs/FBlogList";
export default {
  name: "Index",
  components: { FBlogList },
  layout: "guest",
  auth: false,
  data: () => ({
    dialog: false,
    dialogKey: 0,
  }),
};
</script>

<style scoped></style>
