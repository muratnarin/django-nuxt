<template>
  <v-row>
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
        :item-class="(item) => (item.is_active ? '' : 'grey lighten-4')"
        multi-sort
        must-sort
      >
        <!--        <template #top>-->
        <!--          <v-toolbar dense flat>-->
        <!--            <v-toolbar-title>{{ $t("label.users") }}</v-toolbar-title>-->
        <!--            <v-spacer> </v-spacer>-->
        <!--            <v-btn small color="primary" @click="addItem"-->
        <!--              ><v-icon left>mdi-plus</v-icon>-->
        <!--              {{ $t("button.add") }}-->
        <!--            </v-btn>-->
        <!--          </v-toolbar>-->
        <!--        </template>-->
        <template #item.fullName="{ item }">
          <v-list-item class="px-0">
            <v-list-item-avatar size="30px">
              <img v-if="item.avatar" alt="Avatar" :src="item.avatar" />
              <v-icon
                v-else
                :color="item.color"
                v-text="'mdi-account'"
              ></v-icon>
            </v-list-item-avatar>
            <v-list-item-content>
              <v-list-item-title>{{
                item.first_name + " " + item.last_name
              }}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </template>
        <template #item.actions="{ item }">
          <!--          <v-icon small color="success" @click="editItem(item)"-->
          <!--            >mdi-pencil-outline</v-icon-->
          <!--          >-->

          <v-icon small color="error" @click="deleteItem(item)"
            >mdi-delete-outline</v-icon
          >
          <v-icon
            v-if="!item.is_send_crm"
            small
            color="success"
            title="add to crm"
            @click="sendCrm(item)"
            >mdi-plus-circle</v-icon
          >
        </template>
      </v-data-table>
      <confirm-dialog ref="confirm"></confirm-dialog>
      <v-dialog :key="dialogKey" v-model="dialog" width="800" persistent>
        <user-dialog
          :item-id="itemId"
          :edited-index="editedIndex"
          :form-title="formTitle"
          :item-name="itemName"
          @close="closeDialog"
          @save="save"
        ></user-dialog>
      </v-dialog>
    </v-col>
  </v-row>
</template>

<script>
import { crudMixin } from "~/mixins/crudMixin";

import ConfirmDialog from "~/components/dialogs/CConfirmDialog";
import UserDialog from "~/components/dialogs/UserDialog";

export default {
  name: "Users",
  components: { UserDialog, ConfirmDialog },
  mixins: [crudMixin],
  layout: "authenticated",
  data: () => ({
    itemName: "user",
    expand: false,
    headers: [
      { text: "user", value: "fullName" },
      { text: "email", value: "email" },
      { text: "phone", value: "telephone" },
      { text: "actions", value: "actions", sortable: false, width: "100px" },
    ],
    jobs: [],
  }),
  methods: {
    async sendCrm(item) {
      this.loading = true;
      try {
        await this.$axios.post(`/api/savetocrm/`, {
          first_name: item.first_name,
          last_name: item.last_name,
          email: item.email,
        });
        this.$toast("Successfully Added to Crm", 2);
        await this.fetchItems();
      } catch (e) {
        this.loading = false;
        this.$toast("Error occured while adding to Crm", 1);
      }
    },
  },
};
</script>
