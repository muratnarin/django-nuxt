<template>
  <v-card>
    <v-card-text>
      <v-row>
        <v-col cols="12" lg="7">
          <!--          <v-carousel-->
          <!--            v-model="slide"-->
          <!--            :show-arrows="false"-->
          <!--            cycle-->
          <!--            hide-delimiter-background-->
          <!--            interval="3000"-->
          <!--          >-->
          <!--            <v-carousel-item-->
          <!--              v-for="(currentItem, i) in items"-->
          <!--              :key="i"-->
          <!--              :src="currentItem.src"-->
          <!--            ></v-carousel-item>-->
          <!--          </v-carousel>-->
          <!--          <v-row dense class="mt-1">-->
          <!--            <v-col-->
          <!--              v-for="(img, i) in items"-->
          <!--              :key="i * 10"-->
          <!--              cols="3"-->
          <!--              class="pointer"-->
          <!--              @click="slide = i"-->
          <!--            >-->
          <!--              <v-img :src="img.src" height="100"></v-img>-->
          <!--            </v-col>-->
          <!--          </v-row>-->
          <v-img :src="item.image || '/school.jpeg'"></v-img>
        </v-col>

        <v-col>
          <v-card flat class="d-flex flex-column fill-height">
            <v-card-title class="pt-0 px-0">
              {{ item[$localize("title")] }}
              <v-spacer></v-spacer>
              <v-card-subtitle
                class="py-1 px-0 d-flex align-center text--disabled"
              >
                <v-icon small color="grey">mdi-map-marker</v-icon
                >{{ item.city_name || "- " }}/
                {{ item[$localize("country_name")] }}</v-card-subtitle
              >
            </v-card-title>
            <v-divider></v-divider>
            <v-card-text class="flex-grow-1">
              <div v-html="item[$localize('description')]"></div>
            </v-card-text>
            <v-divider></v-divider>
            <v-card-title
              class="px-0 pb-1 d-flex align-center deep-purple--text"
            >
              <v-icon class="mr-1">mdi-tag-outline</v-icon>
              {{
                formatPrice(item.price) +
                " " +
                (item[$localize("price_unit_name")] || "TL")
              }}
              <v-spacer></v-spacer>
              <v-btn small color="primary">{{ $t("button.apply") }}</v-btn>
            </v-card-title>
          </v-card>
        </v-col>
      </v-row>
    </v-card-text>
  </v-card>
</template>

<script>
import round from "lodash/round";
export default {
  name: "FSchoolDetail",
  props: {
    item: {
      type: Object,
      default: () => ({}),
    },
  },
  data: () => ({
    slide: 0,
  }),
  methods: {
    formatPrice(price) {
      return round(price, 2);
    },
  },
};
</script>
