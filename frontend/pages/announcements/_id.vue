<template>
  <v-container class="py-16">
    <v-row v-if="!$fetchState.pending" no-gutters>
      <v-col cols="12">
        <v-btn
          text
          plain
          left
          to="/announcements"
          class="text-capitalize px-0 py-1 mb-3"
        >
          <v-icon>mdi-arrow-left</v-icon>
          <div class="text-h6">{{ $t("label.announcements") }}</div>
        </v-btn>
      </v-col>
      <v-col cols="12">
        <f-announcement-detail :item="item"></f-announcement-detail>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { detailMixin } from "~/mixins/detailMixin";
import FAnnouncementDetail from "~/components/announcements/FAnnouncementDetail";

export default {
  name: "Id",
  components: { FAnnouncementDetail },
  mixins: [detailMixin],
  layout: "guest",
  auth: false,
  data: () => ({
    itemName: "announcements",
    item: {},
    jobs: [],
    permissions: [
      {
        text: "POS Access",
        selected: false,
        subItems: [
          { id: 1, text: "Table service mode", value: true, override: false },
          { id: 2, text: "Table service mode", value: false, override: true },
          { id: 3, text: "Table service mode", value: true, override: false },
          { id: 4, text: "Table service mode", value: false, override: true },
        ],
      },
      {
        text: "Delivery Access",
        selected: false,
        subItems: [],
      },
    ],
    headers: [
      { text: "Permission", value: "text" },
      { text: "Inherit", value: "override" },
      { text: "Actions", value: "actions" },
    ],
  }),
  async fetch() {
    const { id } = this.$route.params;
    try {
      this.item = await this.$axios.$post("/api/getannouncementbyid/", {
        slug: id,
      });
    } catch (e) {
      this.$handleError(e);
    }
  },
  methods: {
    selectAll(group) {
      const val = !!group.subItems.some((item) => !item.value);
      group.subItems.forEach((item) => {
        item.value = val;
      });
      group.selected = val;
    },
    checkAll(group) {
      group.selected = !!group.subItems.every((item) => item.value);
    },
  },
};
</script>
