<template>
  <div v-if="!$fetchState.pending">
    <v-img height="600" :src="banner.file">
      <v-row justify="center" class="fill-height">
        <v-col cols="12" md="6" align-self="center">
          <v-overlay absolute opacity="0.6" class="w-100">
            <v-card light color="transparent" flat>
              <v-card-title class="justify-center w-100 text-break">
                <span class="text-h4 white--text text-center">{{
                  $t("label.bannerTitle")
                }}</span>
              </v-card-title>
              <div class="d-flex">
                <v-select
                  v-model="options.type"
                  :items="types"
                  item-value="id"
                  :item-text="$localize('display_name')"
                  :placeholder="$t('label.schoolType')"
                  hide-details
                  solo
                  class="mr-2"
                  color="primary"
                  clearable
                ></v-select>
                <v-text-field
                  v-model="options.search"
                  hide-details
                  solo
                  class="pr-0 w-100"
                  :placeholder="$t('label.searchPlaceholder')"
                >
                  <template #prepend> </template>
                  <template #append>
                    <v-btn text plain color="purple" @click="fetchSchools">
                      <v-icon left class="mr-1">mdi-magnify</v-icon
                      >{{ $t("label.search") }}</v-btn
                    >
                  </template>
                </v-text-field>
              </div>
            </v-card>
          </v-overlay>
        </v-col>
      </v-row>
    </v-img>
    <!--    <f-slider></f-slider>-->
    <v-card color="grey lighten-4">
      <v-container>
        <v-card-title
          class="justify-center text-h4 py-7 text-break text-center"
        >
          {{ $t("label.exchangePrograms") }}
        </v-card-title>
        <v-card-text>
          <v-row dense>
            <v-col v-for="item in items" :key="item.id" cols="12" lg="4" sm="6">
              <f-service-card :item="item"></f-service-card>
            </v-col>
          </v-row>
        </v-card-text>
      </v-container>
    </v-card>
    <v-card>
      <v-container>
        <v-card-title class="justify-center text-h4 py-7 text-break text-center"
          >{{ $t("label.languageSchools") }}
        </v-card-title>
        <v-card-text class="pb-10">
          <v-row dense>
            <v-col
              v-for="school in schools"
              :key="school.id"
              cols="12"
              lg="3"
              md="4"
              sm="6"
            >
              <f-image-card :item="school"></f-image-card>
            </v-col>
          </v-row>
        </v-card-text>
      </v-container>
    </v-card>
    <v-card color="grey lighten-3">
      <v-container>
        <v-card-title
          class="justify-center text-h4 py-7 text-break text-center"
        >
          {{ $t("label.latestNews") }}
        </v-card-title>
        <v-card-text>
          <v-row dense>
            <v-col
              v-for="announcement in announcements"
              :key="announcement.id"
              cols="12"
              lg="3"
            >
              <f-announcement-list-card
                :item="announcement"
              ></f-announcement-list-card>
            </v-col>
          </v-row>
        </v-card-text>
      </v-container>
    </v-card>
  </div>
</template>

<script>
import FServiceCard from "~/components/home/FServiceCard";
import FImageCard from "~/components/home/FImageCard";
import FAnnouncementListCard from "~/components/announcements/FAnnouncementListCard";
export default {
  name: "Index",
  components: { FAnnouncementListCard, FImageCard, FServiceCard },
  layout: "guest",
  data: () => ({
    value: 0,
    items: [],
    schools: [],
    announcements: [],
    types: [],
    options: {},
    banner: {},
    contact: {},
  }),
  async fetch() {
    try {
      const { result: exchangePrograms } = await this.$axios.$post(
        "/api/getexchangeprograms/"
      );
      this.schools = await this.$axios.$post("/api/getmainpageschools/");
      const { result: announcements } = await this.$axios.$post(
        "/api/getannouncements/",
        {
          itemsPerPage: 4,
        }
      );

      const { result: parameters } = await this.$axios.$post(
        `/api/getparameters/`,
        {
          itemsPerPage: "-1",
          parameter_name_filters: ["type"],
        }
      );
      const { result: banners } = await this.$axios.$post(`/api/getbanners/`, {
        itemsPerPage: "-1",
      });
      this.items = exchangePrograms;
      this.announcements = announcements;
      this.types = parameters;
      this.banner = banners[0] || {};
    } catch (e) {
      this.$handleError(e);
    }
  },
  methods: {
    fetchSchools() {
      if (this.options.type) {
        this.$store.commit("filters/setType", this.options.type);
      }
      if (this.options.search) {
        this.$store.commit("filters/setSearch", this.options.search);
      }
      this.$router.push("/schools");
    },
  },
};
</script>

<style scoped></style>
