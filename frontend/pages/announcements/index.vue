<template>
  <v-container :fluid="$vuetify.breakpoint.mdAndDown" class="pt-16">
    <v-row>
      <v-col><f-announcement-list></f-announcement-list> </v-col>
    </v-row>
  </v-container>
</template>

<script>
import FAnnouncementList from "~/components/announcements/FAnnouncementList";
export default {
  name: "Index",
  components: { FAnnouncementList },
  layout: "guest",
  auth: false,
  data: () => ({
    dialog: false,
    dialogKey: 0,
  }),
};
</script>

<style scoped></style>
