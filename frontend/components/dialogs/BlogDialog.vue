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
            <v-col md="8" class="d-flex align-center">
              <div class="mr-5">
                <img
                  v-if="item.image || image"
                  :src="previewImage"
                  width="150"
                />
                <v-icon v-else size="50">mdi-image</v-icon>
              </div>

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
                v-model="image"
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
            <v-col md="12">
              <c-text-field
                v-model="item.slug"
                rules="required|alpha_dash"
                name="label.slug"
              ></c-text-field>
            </v-col>
            <v-col md="6">
              <c-text-field
                v-model="item.title_tr"
                rules="required"
                :label="$t('label.title') + ' (TR)'"
                name="label.title_tr"
                hide-details
              ></c-text-field>
            </v-col>
            <v-col md="6">
              <c-text-field
                v-model="item.title_en"
                rules="required"
                :label="$t('label.title') + ' (EN)'"
                name="label.title_en"
                hide-details
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
              ></c-text-area>
            </v-col>

            <v-col lg="6">
              <label class="subtitle-1">{{ $t("label.content") }} (TR)</label>
              <editor
                v-model="item.description_tr"
                api-key="hq3zapbuatc0xbapvcbb5reergmteu0g4tmqoqsiwtbtmb0d"
                :init="{
                  height: 300,
                  menubar: false,
                  plugins: [
                    'advlist autolink lists link image charmap print preview anchor',
                    'searchreplace visualblocks code fullscreen',
                    'insertdatetime media table paste code help wordcount',
                  ],
                  toolbar:
                    'undo redo | formatselect | bold italic backcolor | \
           alignleft aligncenter alignright alignjustify | \
           bullist numlist outdent indent | removeformat | help',
                }"
              />
            </v-col>
            <v-col lg="6">
              <label class="subtitle-1">{{ $t("label.content") }} (En)</label>
              <editor
                v-model="item.description_en"
                api-key="hq3zapbuatc0xbapvcbb5reergmteu0g4tmqoqsiwtbtmb0d"
                :init="{
                  height: 300,
                  menubar: false,
                  plugins: [
                    'advlist autolink lists link image charmap print preview anchor',
                    'searchreplace visualblocks code fullscreen',
                    'insertdatetime media table paste code help wordcount',
                  ],
                  toolbar:
                    'undo redo | formatselect | bold italic backcolor | \
           alignleft aligncenter alignright alignjustify | \
           bullist numlist outdent indent | removeformat | help',
                }"
              />
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

export default {
  name: "BlogDialog",
  components: {
    CTextArea,
    CTextField,
    Editor,
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
    image: null,
    currentImage: undefined,
    previewImage: undefined,
  }),
  async fetch() {
    if (this.itemId) {
      this.item = await this.$axios.$post(
        `/api/get${this.itemName.toLowerCase()}byid/`,
        {
          id: this.itemId,
        }
      );
      if (this.item.image) {
        this.previewImage = this.item.image;
      }
    }
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
        if (this.image instanceof File) {
          formData.append("image", this.image);
        }
        if (this.item.id) {
          formData.append("id", this.item.id);
        }
        formData.append("slug", this.item.slug);
        formData.append("title_tr", this.item.title_tr);
        formData.append("title_en", this.item.title_en);
        formData.append("summary_tr", this.item.summary_tr);
        formData.append("summary_en", this.item.summary_en);
        formData.append("description_tr", this.item.description_tr);
        formData.append("description_en", this.item.description_en);

        this.$emit("save", formData);
      }
    },
  },
};
</script>

<style scoped></style>
