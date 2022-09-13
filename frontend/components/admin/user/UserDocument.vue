<template>
  <v-col cols="12" lg="6">
    <v-card flat outlined>
      <v-card-text>
        <div class="d-flex align-center">
          <v-icon large>mdi-file-document-outline</v-icon>
          <div class="ml-3">
            <div class="mt-1 text-subtitle-2">Adres_document.pdf</div>
            <div class="text-caption">6MB - 26.04.2022</div>
          </div>
          <v-spacer></v-spacer>
          <v-btn text plain small @click="deleteItem">{{
            $t("button.delete")
          }}</v-btn>
        </div>
      </v-card-text>
    </v-card>
    <confirm-dialog ref="confirm"></confirm-dialog>
  </v-col>
</template>

<script>
import ConfirmDialog from "~/components/dialogs/CConfirmDialog";
export default {
  name: "UserDocument",
  components: { ConfirmDialog },
  prop: {
    item: {
      type: Object,
      default: () => ({}),
    },
  },
  data: () => ({
    deleteMessage: "this item",
    itemName: "users",
  }),
  methods: {
    async confirmDelete(id) {
      try {
        await this.$axios.$delete(`/cms/${this.itemName.toLowerCase()}/${id}`);
        this.$toast("Successfully Deleted", 2);
        await this.fetchItems();
      } catch (e) {
        this.$handleError(e);
      }
    },
    async deleteItem(item) {
      if (
        await this.$refs.confirm.open(
          `Are you sure you want to <b>delete</b> ${this.deleteMessage}?`
        )
      ) {
        await this.confirmDelete(item.id);
      }
    },
  },
};
</script>

<style scoped></style>
