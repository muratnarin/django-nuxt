<template>
  <v-container :fluid="$vuetify.breakpoint.mdAndDown" class="pt-16">
    <v-row v-if="!$fetchState.pending">
      <v-col cols="12" md="4" lg="3">
        <v-card-title class="px-0">{{ $t("label.filters") }}</v-card-title>
        <v-card flat outlined>
          <v-card-text class="py-2">
            <v-text-field
              v-model="options.search"
              :label="$t('label.search')"
              clearable
              class="mt-1"
            ></v-text-field>
            <v-select
              v-model="options.type"
              :items="types"
              item-value="id"
              :item-text="$localize('display_name')"
              :label="$t('label.schoolType')"
            >
            </v-select>
            <v-select
              v-model="options.country"
              :items="countries"
              :item-text="$i18n.locale === 'en' ? 'name_en' : 'name_tr'"
              item-value="id"
              :label="$t('label.country')"
              @change="getCities"
            >
            </v-select>
            <v-select
              v-model="options.city"
              :items="cities"
              item-text="name"
              item-value="id"
              :label="$t('label.city')"
              :disabled="!options.country"
            >
            </v-select>
            <v-range-slider
              v-model="options.price_range"
              :max="max"
              :min="min"
              thumb-label="always"
              :label="$t('label.price')"
              class="mt-5"
            >
              <template #thumb-label="{ value }">
                {{ value >= 1000 ? value / 1000 + "K" : value }}
              </template>
            </v-range-slider>
          </v-card-text>
          <v-card-actions>
            <v-btn text @click="reset">{{ $t("button.reset") }}</v-btn>
            <v-spacer></v-spacer>
            <v-btn color="deep-purple" dark @click="getFilteredSchools">{{
              $t("button.filter")
            }}</v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
      <v-col cols="12" md="8" lg="9">
        <v-card-title class="px-0"
          >{{ $t("label.schools") }}<v-spacer></v-spacer>
          <v-pagination
            v-model="options.page"
            :length="Math.ceil(total / options.itemsPerPage)"
            :color="$vuetify.theme.dark ? 'grey' : 'primary'"
            @input="$fetch"
          ></v-pagination
        ></v-card-title>
        <v-card flat>
          <v-card-text class="pa-0">
            <v-row>
              <v-col
                v-for="item in items"
                :key="item.id"
                class="isotope-item"
                cols="12"
                lg="4"
              >
                <f-school-card :item="item"></f-school-card>
              </v-col>
            </v-row>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import FSchoolCard from "~/components/schools/FSchoolCard";
export default {
  name: "Index",
  auth: false,
  components: { FSchoolCard },
  layout: "guest",
  data: () => ({
    items: [],
    total: [],
    countries: [],
    cities: [],
    types: [],
    options: { itemsPerPage: 6, page: 1 },
    max: 10000,
    min: 0,
  }),
  async fetch() {
    if (this.$store.state.filters.type) {
      this.options.type = this.$store.state.filters.type;
    }
    if (this.$store.state.filters.country) {
      this.options.country = this.$store.state.filters.country;
      await this.getCities();
    }
    if (this.$store.state.filters.city) {
      this.options.city = this.$store.state.filters.city;
    }
    if (this.$store.state.filters.price_range?.length) {
      this.options.price_range = this.$store.state.filters.price_range;
    }
    if (this.$store.state.filters.search) {
      this.options.search = this.$store.state.filters.search;
    }
    const { result: parameters } = await this.$axios.$post(
      `/api/getparameters/`,
      {
        itemsPerPage: "-1",
        parameter_name_filters: ["type"],
      }
    );
    const { result: countries } = await this.$axios.$post(`/api/getcountrys/`, {
      itemsPerPage: "-1",
    });
    const { min, max } = await this.$axios.$post(`/api/getpricerange/`);
    this.min = Math.floor(min);
    this.max = Math.ceil(max);
    this.options.price_range = [min, max];
    const { total, result } = await this.$axios.$post("/api/getschools/", {
      ...this.options,
    });
    this.items = result;
    this.total = total;
    this.countries = countries;
    this.types = parameters;
  },
  beforeDestroy() {
    this.$store.commit("filters/setType", "");
    this.$store.commit("filters/setCountry", "");
    this.$store.commit("filters/setCity", "");
    this.$store.commit("filters/setPriceRange", []);
    this.$store.commit("filters/setSearch", "");
  },
  methods: {
    async getFilteredSchools() {
      const { total, result } = await this.$axios.$post("/api/getschools/", {
        ...this.options,
      });
      this.items = result;
      this.total = total;
      const { min, max } = await this.$axios.$post(`/api/getpricerange/`);
      this.min = Math.floor(min);
      this.max = Math.ceil(max);
      this.options.price_range = [min, max];
    },
    async reset() {
      this.options = { itemsPerPage: 6, page: 1 };
      await this.getFilteredSchools();
    },
    async getCities(countryId) {
      const { result } = await this.$axios.$post(`/api/getcitys/`, {
        country_id: countryId,
        itemsPerPage: "-1",
      });
      this.cities = result;
    },
  },
};
</script>

<style scoped></style>
