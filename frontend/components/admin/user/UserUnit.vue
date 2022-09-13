<template>
  <v-card class="mt-5">
    <v-card-title>
      <div class="text-h6 d-flex align-center flex-grow-1">
        <v-icon color="purple" class="mr-3">mdi-account-group-outline</v-icon>
        <div>
          User's Units
          <!--            <div class="subtitle-1">
              “*” ile gösterilen alanları doldurmak zorunludur.
            </div>-->
        </div>
        <v-spacer></v-spacer>

        <c-select
          v-model="unit"
          dense
          :items="items"
          item-key="id"
          item-text="name"
          hide-details
          full-width
          label="Select Unit"
        ></c-select>
      </div>
    </v-card-title>
  </v-card>
</template>

<script>
import CSelect from "~/components/form/CSelect";
export default {
  name: "UserUnit",
  components: { CSelect },
  props: {
    item: {
      type: Object,
      default: () => ({}),
    },
  },
  data: () => ({
    items: [
      {
        id: 1,
        name: "Unit 1",
      },
      {
        id: 2,
        name: "Unit 2",
      },
      {
        id: 3,
        name: "Unit 3",
      },
    ],
    unit: "",
  }),
  created() {
    if (this.item) {
      this.unit = this.item.unit;
    }
  },
};
</script>

<style scoped></style>
