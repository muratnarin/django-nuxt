<template>
  <v-card height="350" rounded class="d-flex flex-column">
    <v-img
      class="white--text align-start"
      :src="item.image ? item.image : '/school.jpeg'"
      max-height="150"
    >
    </v-img>
    <div class="flex-grow-1 overflow-auto mt-4">
      <div class="text-truncate body-1 font-weight-medium px-4">
        {{ item[$localize("title")] }}
      </div>
      <v-card-subtitle class="py-1 px-3 d-flex align-center text--disabled">
        <v-icon small color="grey">mdi-map-marker</v-icon>
        {{ item.city_name || "- " }}/
        {{ item[$localize("country_name")] }}</v-card-subtitle
      >

      <v-card-text>
        <v-clamp autoresize :max-lines="3">
          {{ item[$localize("summary")] }}
        </v-clamp>
      </v-card-text>
    </div>

    <v-card-actions class="py-1">
      <v-card-subtitle class="px-1 py-1 d-flex align-center">
        <v-icon small class="mr-1">mdi-tag-outline</v-icon>
        {{
          formatPrice(item.price) +
          " " +
          (item[$localize("price_unit_name")] || "TL")
        }}
      </v-card-subtitle>
      <v-spacer></v-spacer>
      <v-btn color="indigo" text small :to="`/schools/${item.slug}`">
        {{ $t("button.details") }}
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
import round from "lodash/round";
import VClamp from "vue-clamp";
export default {
  name: "FSchoolCard",
  components: {
    VClamp,
  },
  props: {
    item: {
      type: Object,
      default: () => ({}),
    },
  },
  methods: {
    formatPrice(price) {
      return round(price, 2);
    },
  },
};
</script>
