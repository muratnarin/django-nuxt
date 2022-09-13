<template>
  <div>
    <v-card-title class="px-0">{{ $t("label.announcements") }}</v-card-title>
    <v-card flat>
      <v-card-text class="pa-0">
        <v-row>
          <v-col v-for="item in items" :key="item.id" cols="12" lg="3">
            <f-announcement-list-card :item="item"></f-announcement-list-card>
          </v-col>
        </v-row>
      </v-card-text>
    </v-card>
  </div>
</template>

<script>
import FAnnouncementListCard from "~/components/announcements/FAnnouncementListCard";
export default {
  name: "FAnnouncementList",
  components: { FAnnouncementListCard },
  data: () => ({
    items: [],
    total: [],
  }),
  async fetch() {
    const { total, result } = await this.$axios.$post("/api/getannouncements/");
    this.items = result;
    this.total = total;
  },
  created() {},
  methods: {},
};
</script>
