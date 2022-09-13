<template>
  <v-container :fluid="$vuetify.breakpoint.mdAndDown" class="pt-16">
    <v-row>
      <v-col cols="12">
        <GmapMap
          :center="{ lat: 41.015137, lng: 28.97953 }"
          :zoom="14"
          map-type-id="terrain"
          style="width: 100%; height: 500px"
        >
          <GmapMarker
            v-for="(m, index) in markers"
            :key="index"
            :position="m.position"
            :clickable="true"
            :draggable="true"
            @click="center = m.position"
          />
        </GmapMap>
      </v-col>
    </v-row>

    <v-row dense class="mt-10">
      <v-col cols="12" lg="8">
        <v-card-title class="px-0">{{ $t("label.contactForm") }}</v-card-title>
        <client-only>
          <div v-once id="hubspotForm"></div>
        </client-only>
      </v-col>
      <v-col>
        <v-card flat>
          <v-card-title>{{ $t("label.contactInfo") }}</v-card-title>
          <v-card-text v-for="item in items.slice(0, 1)" :key="item.id">
            <div class="subtitle-1 py-2 ml-1">
              <v-icon class="mr-1">mdi-map-marker</v-icon
              >{{ item[$localize("address")] }}
            </div>
            <div>
              <v-icon class="mr-1 py-2 ml-1">mdi-email</v-icon>{{ item.email }}
            </div>
            <div class="d-flex py-2">
              <v-btn icon :href="'https://' + item.linkedin" target="_blank">
                <v-icon>mdi-linkedin</v-icon>
              </v-btn>
              <v-btn icon :href="'https://' + item.facebook" target="_blank">
                <v-icon>mdi-facebook</v-icon>
              </v-btn>
              <v-btn icon :href="'https://' + item.instagram" target="_blank">
                <v-icon>mdi-instagram</v-icon>
              </v-btn>
              <v-btn icon :href="'https://' + item.pinterest" target="_blank">
                <v-icon>mdi-pinterest</v-icon>
              </v-btn>
              <v-btn icon :href="'https://' + item.youtube" target="_blank">
                <v-icon>mdi-youtube</v-icon>
              </v-btn>
              <v-btn icon :href="'https://' + item.twitter" target="_blank">
                <v-icon>mdi-twitter</v-icon>
              </v-btn>
            </div>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "Index",
  layout: "guest",
  auth: false,
  data: () => ({
    center: { lat: 4.5, lng: 99 },
    markers: [],
    items: [],
    total: 0,
    contact: {},
  }),
  async fetch() {
    const { result, total } = await this.$axios.$post("/api/getcontacts/");
    this.items = result;
    this.total = total;
  },
  mounted() {
    const script = document.createElement("script");
    script.src = "https://js.hsforms.net/forms/v2.js";
    document.body.appendChild(script);
    script.addEventListener("load", () => {
      if (window.hbspt) {
        window.hbspt.forms.create({
          region: "na1",
          portalId: "5694482",
          formId: "093e2aaa-d16b-4d15-be8b-98c31bbaf37b",
          target: "#hubspotForm",
        });
      }
    });
  },
  methods: {
    async submit() {
      const success = await this.$refs.cForm.validate();
      if (success) {
        this.loading = true;
        try {
          await this.$axios.$post("/api/createcontact/", this.contact);
        } catch (e) {
          this.$toast(e.response.data.detail, 1);
        } finally {
          this.loading = false;
        }
      }
    },
  },
};
</script>

<style scoped></style>
