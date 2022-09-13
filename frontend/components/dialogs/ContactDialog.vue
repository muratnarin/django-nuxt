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
              <c-text-field
                v-model="item.phone"
                rules="required"
                name="label.phone"
                hide-details
              ></c-text-field>
            </v-col>
            <v-col md="6">
              <c-text-field
                v-model="item.email"
                rules="required"
                name="label.email"
                hide-details
              ></c-text-field>
            </v-col>
            <v-col md="6">
              <c-text-field
                v-model="item.address_tr"
                rules="required"
                name="label.address"
                :label="$t('label.address') + ' (TR)'"
                hide-details
              ></c-text-field>
            </v-col>
            <v-col md="6">
              <c-text-field
                v-model="item.address_en"
                rules="required"
                name="label.address"
                :label="$t('label.address') + ' (EN)'"
                hide-details
              ></c-text-field>
            </v-col>
            <v-col md="6">
              <c-text-field
                v-model="item.linkedin"
                rules="required"
                name="label.linkedin"
                placeholder="www.linkedin.com/in/..."
                hide-details
              ></c-text-field>
            </v-col>
            <v-col md="6">
              <c-text-field
                v-model="item.facebook"
                rules="required"
                name="label.facebook"
                placeholder="www.facebook.com/..."
                hide-details
              ></c-text-field>
            </v-col>
            <v-col md="6">
              <c-text-field
                v-model="item.instagram"
                rules="required"
                name="label.instagram"
                placeholder="www.instagram.com/..."
                hide-details
              ></c-text-field>
            </v-col>
            <v-col md="6">
              <c-text-field
                v-model="item.twitter"
                rules="required"
                name="label.twitter"
                placeholder="www.twitter.com/..."
                hide-details
              ></c-text-field>
            </v-col>
            <v-col md="6">
              <c-text-field
                v-model="item.pinterest"
                rules="required"
                name="label.pinterest"
                placeholder="www.pinterest.com/..."
                hide-details
              ></c-text-field>
            </v-col>
            <v-col md="6">
              <c-text-field
                v-model="item.tiktok"
                rules="required"
                name="label.tiktok"
                placeholder="www.tiktok.com/..."
                hide-details
              ></c-text-field>
            </v-col>
            <v-col md="6">
              <c-text-field
                v-model="item.youtube"
                rules="required"
                name="label.youtube"
                placeholder="www.youtube.com/..."
                hide-details
              ></c-text-field>
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
import CTextField from "~/components/form/CTextField";

export default {
  name: "ContactDialog",
  components: {
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
