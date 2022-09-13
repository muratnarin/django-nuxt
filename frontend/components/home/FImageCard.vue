<template>
  <v-hover v-slot="{ hover }">
    <v-img
      :src="item.image ? item.image : '/1015-320x300.jpeg'"
      class="white--text align-center image-card rounded pointer"
      @click="getSchoolsByCountry"
    >
      <v-overlay :value="true" absolute :opacity="hover ? '0.8' : '0.4'">
        <div class="country-count d-flex text-h6">
          <v-icon class="mr-2">mdi-school</v-icon>
          {{ item.count }}
        </div>
        <v-row class="fill-height ma-0 text-h6" align="center" justify="center">
          {{ item[$localize("name")] }}
        </v-row>
      </v-overlay>
    </v-img>
  </v-hover>
</template>

<script>
export default {
  name: "FImageCard",
  props: {
    item: {
      type: Object,
      default: () => ({}),
    },
  },
  methods: {
    async getSchoolsByCountry() {
      await this.$store.commit("filters/setCountry", this.item.id);
      await this.$router.push("/schools");
    },
  },
};
</script>

<style>
.country-count {
  position: absolute;
  top: 5px;
  right: 10px;
}
.image-card .v-overlay__content {
  width: 100%;
  height: 100%;
}
</style>
