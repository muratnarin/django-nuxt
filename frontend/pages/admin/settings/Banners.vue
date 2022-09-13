<template>
  <v-container :fluid="$vuetify.breakpoint.mdAndDown" class="pt-16">
    <v-row>
      <v-col>
        <ValidationObserver ref="cForm" v-slot="{ handleSubmit }">
          <v-card
            :loading="$fetchState.pending"
            max-height="80vh"
            class="d-flex flex-column"
          >
            <v-card-title>
              {{ $t("label.banners") }}
            </v-card-title>

            <v-card-text
              v-if="!$fetchState.pending"
              class="flex-grow-1 overflow-auto"
            >
              <v-form>
                <v-row>
                  <v-col md="12" class="">
                    <div class="mr-5">
                      <img v-if="item.file" :src="previewImage" width="150" />
                      <v-icon v-else size="50">mdi-image</v-icon>
                    </div>

                    <div class="text-h6">
                      {{
                        $i18n.locale === "en" ? "Add Banner" : "Banner  Ekle"
                      }}
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
                      v-model="file"
                      label="Select Image"
                      accept="image/*"
                      prepend-icon=""
                      hide-input
                      @change="selectImage"
                    >
                    </v-file-input>
                  </v-col>
                </v-row>
              </v-form>
            </v-card-text>

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn class="primary" @click="handleSubmit(save)">
                {{ $t("button.save") }}
              </v-btn>
            </v-card-actions>
          </v-card>
        </ValidationObserver>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "Banners",
  layout: "authenticated",
  data: () => ({
    file: null,
    itemName: "banner",
    item: {},
    currentImage: undefined,
    previewImage: undefined,
  }),
  async fetch() {
    try {
      const { result } = await this.$axios.$post("/api/getbanners/", {
        itemsPerPage: "-1",
      });
      if (result.length > 0) {
        this.item = result[0];
      }
      if (this.item.file) {
        this.previewImage = this.item.file;
      }
    } catch (e) {
      this.$handleError(e);
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
        if (this.file instanceof File) {
          formData.append("file", this.file);
        }
        if (this.item?.id) {
          formData.append("id", this.item.id);
        }
        try {
          await this.$axios.$post(
            `/api/${this.item?.id ? "update" : "create"}banner/`,
            formData
          );
          await this.$fetch();
        } catch (e) {
          this.$handleError(e);
        }
      }
    },
  },
};
</script>

<style scoped></style>
