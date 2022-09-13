<template>
  <ValidationObserver ref="cForm" v-slot="{ handleSubmit }">
    <v-card
      :loading="$fetchState.pending"
      max-height="80vh"
      class="d-flex flex-column"
    >
      <v-card-title>
        {{ formTitle }}
      </v-card-title>

      <v-card-text
        v-if="!$fetchState.pending"
        class="flex-grow-1 overflow-auto"
      >
        <v-form>
          <v-row>
            <v-col md="6">
              <c-select
                v-model="item.icon"
                :items="icons"
                rules="required"
                name="label.icon"
                hide-details
              >
                <template #selection="{ item }">
                  <v-icon class="mr-2">{{ item }}</v-icon> {{ item }}
                </template>
                <template #item="{ item }">
                  <v-icon class="mr-2">{{ item }}</v-icon> {{ item }}
                </template>
              </c-select>
            </v-col>
            <v-col md="6">
              <c-select
                v-model="item.icon_color"
                :items="colors"
                rules="required"
                name="label.iconColor"
                hide-details
              >
                <template #selection="{ item }">
                  <v-icon class="mr-2" :color="item">mdi-circle</v-icon>
                  {{ item }}
                </template>
                <template #item="{ item }">
                  <v-icon class="mr-2" :color="item">mdi-circle</v-icon>
                  {{ item }}
                </template>
              </c-select>
            </v-col>
            <v-col md="6">
              <c-text-field
                v-model="item.title_tr"
                rules="required"
                name="label.title"
                :label="$t('label.title') + ' (TR)'"
                hide-details
              ></c-text-field>
            </v-col>
            <v-col md="6">
              <c-text-field
                v-model="item.title_en"
                rules="required"
                name="label.title"
                :label="$t('label.title') + ' (EN)'"
              ></c-text-field>
            </v-col>

            <v-col md="6">
              <c-text-area
                v-model="item.summary_tr"
                rules="required|max:150"
                name="label.summary_tr"
                :label="$t('label.summary') + ' (TR)'"
              ></c-text-area>
            </v-col>
            <v-col md="6">
              <c-text-area
                v-model="item.summary_en"
                rules="required|max:150"
                name="label.summary_en"
                :label="$t('label.summary') + ' (EN)'"
                hide-details
              ></c-text-area>
            </v-col>
          </v-row>
        </v-form>
      </v-card-text>

      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn text plain color="error" @click="$emit('close')">{{
          $t("button.cancel")
        }}</v-btn>
        <v-btn class="primary" @click="handleSubmit(save)">
          {{ $t(editedIndex === -1 ? "button.save" : "button.edit") }}
        </v-btn>
      </v-card-actions>
    </v-card>
  </ValidationObserver>
</template>

<script>
import Editor from "@tinymce/tinymce-vue";
import CTextField from "~/components/form/CTextField";
import CTextArea from "~/components/form/CTextArea";
import CSelect from "~/components/form/CSelect";

export default {
  name: "ExchangeDialog",
  components: {
    CSelect,
    CTextArea,
    CTextField,
  },
  props: {
    itemId: {
      type: [Number, String],
      default: null,
    },
    editedIndex: {
      type: Number,
      default: null,
    },

    formTitle: {
      type: String,
      default: "",
    },
    itemName: {
      type: String,
      default: "",
    },
  },
  data: () => ({
    item: {},
    icons: [
      "mdi-train-car",
      "mdi-campfire",
      "mdi-credit-card-multiple-outline",
      "mdi-book-education",
      "mdi-school-outline",
      "mdi-certificate-outline",
    ],
    colors: ["purple", "warning", "indigo", "success", "error", "teal"],
  }),
  async fetch() {
    if (this.itemId) {
      this.item = await this.$axios.$post(
        `/api/get${this.itemName.toLowerCase()}byid/`,
        {
          id: this.itemId,
        }
      );
    }
  },
  methods: {
    async save() {
      const success = await this.$refs.cForm.validate();
      if (success) {
        this.$emit("save", this.item);
      }
    },
  },
};
</script>

<style scoped></style>
