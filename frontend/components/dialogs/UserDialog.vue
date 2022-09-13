<template>
  <ValidationObserver ref="cForm" v-slot="{ handleSubmit }">
    <v-card :loading="$fetchState.pending">
      <v-card-title>
        {{ formTitle }}
      </v-card-title>

      <v-card-text v-if="!$fetchState.pending">
        <v-form>
          <v-row>
            <v-col md="8" class="d-flex align-center">
              <v-btn
                icon
                outlined
                height="100"
                width="100"
                class="mr-5"
                @click="openUpload"
              >
                <v-avatar size="100">
                  <img
                    v-if="item.avatar || avatar"
                    :src="previewImage"
                    alt=""
                  />
                  <v-icon v-else size="50">mdi-image</v-icon>
                </v-avatar>
              </v-btn>
              <div class="text-h6">
                {{ $i18n.locale === "en" ? "Add Photo" : "Fotoğraf  Ekle" }}
                <div class="text-subtitle-2">
                  {{ $t("text.avatar_size") }}
                </div>
                <v-btn
                  dense
                  text
                  color="primary"
                  class="text-capitalize px-0"
                  @click="openUpload"
                >
                  {{ $t("button.upload") }}
                </v-btn>
              </div>

              <v-file-input
                ref="fileInput"
                v-model="avatar"
                label="Select Image"
                accept="image/*"
                prepend-icon=""
                hide-input
                @change="selectImage"
              >
              </v-file-input>
            </v-col>
          </v-row>

          <v-row>
            <v-col md="6">
              <c-text-field
                v-model="item.first_name"
                rules="required"
                name="label.first_name"
                hide-details
              ></c-text-field>
            </v-col>
            <v-col md="6">
              <c-text-field
                v-model="item.last_name"
                rules="required"
                name="label.last_name"
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
                v-model="item.telephone"
                name="label.phone"
                vid="phone"
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
  name: "UserDialog",
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
    roles: [],
    avatar: null,
    currentImage: undefined,
    previewImage: undefined,
    progress: 0,
    imageInfos: [],
    files: [],
  }),
  async fetch() {
    if (this.itemId) {
      this.item = await this.$axios.$post(
        `/api/get${this.itemName.toLowerCase()}byid/`,
        {
          id: this.itemId,
        }
      );
      if (this.item.avatar) {
        this.previewImage = this.item.avatar;
      }
    }
    const roles = await this.$axios.$get(`/api/roles/`);

    this.roles = roles.items;
  },
  methods: {
    openUpload() {
      this.$refs.fileInput.$refs.input.click();
    },
    openFileUpload() {
      this.$refs.docFileInput.$refs.input.click();
    },
    selectImage(image) {
      this.previewImage = URL.createObjectURL(image);
    },
    async save() {
      const success = await this.$refs.cForm.validate();
      if (success) {
        const formData = new FormData();
        if (this.avatar instanceof File) {
          formData.append("avatar", this.avatar);
        }
        if (this.item.id) {
          formData.append("id", this.item.id);
        }
        formData.append("first_name", this.item.first_name);
        formData.append("last_name", this.item.last_name);
        formData.append("email", this.item.email);
        formData.append("telephone", this.item.telephone);

        this.$emit("save", formData);
      }
    },
  },
};
</script>

<style scoped></style>
