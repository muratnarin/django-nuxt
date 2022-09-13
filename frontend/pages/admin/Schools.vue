<template>
  <v-row v-if="!$fetchState.pending">
    <v-col>
      <v-data-table
        :items="items"
        :headers="localizedHeaders"
        :options.sync="options"
        :server-items-length="total"
        :loading="loading"
        :footer-props="{
          itemsPerPageOptions: [10, 25, 50, 100],
        }"
        multi-sort
        must-sort
      >
        <template #top>
          <v-toolbar dense flat>
            <v-toolbar-title>{{ $t("label.schools") }}</v-toolbar-title>
            <v-spacer> </v-spacer>
            <v-btn small color="primary" @click="addItem"
              ><v-icon left>mdi-plus</v-icon>
              {{ $t("button.add") }}
            </v-btn>
          </v-toolbar>
        </template>
        <template #item.created_at="{ item }">
          {{ formatDate(item.created_at) }}
        </template>
        <template #item.actions="{ item }">
          <v-icon small color="success" @click="editItem(item)"
            >mdi-pencil-outline</v-icon
          >

          <v-icon small color="error" @click="deleteItem(item)"
            >mdi-delete-outline</v-icon
          >
        </template>
      </v-data-table>
      <confirm-dialog ref="confirm"></confirm-dialog>
      <v-dialog :key="dialogKey" v-model="dialog" width="1140" persistent>
        <school-dialog
          :item-id="itemId"
          :edited-index="editedIndex"
          :form-title="formTitle"
          :item-name="itemName"
          @close="closeDialog"
          @save="save"
        ></school-dialog>
      </v-dialog>
    </v-col>
  </v-row>
</template>

<script>
import { crudMixin } from "~/mixins/crudMixin";

import ConfirmDialog from "~/components/dialogs/CConfirmDialog";
import SchoolDialog from "~/components/dialogs/SchoolDialog";

export default {
  name: "Schools",
  components: { SchoolDialog, ConfirmDialog },
  mixins: [crudMixin],
  layout: "authenticated",
  data: () => ({
    itemName: "school",
    expand: false,
    headers: [
      { text: "title", value: "title", localize: true },
      { text: "slug", value: "slug" },
      { text: "price", value: "price" },
      { text: "currency", value: "price_unit_name", localize: true },
      { text: "country", value: "country_name", localize: true },
      { text: "city", value: "city_name" },
      { text: "date", value: "created_at" },
      { text: "actions", value: "actions", sortable: false, width: "100px" },
    ],
    jobs: [],
  }),
  async fetch() {},
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
