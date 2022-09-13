<template>
  <v-card>
    <v-card-text>
      <v-row>
        <v-col cols="12">
          <v-img
            :src="item.image || '/blog.jpeg'"
            height="360"
            width="100%"
            class="align-center text-center"
          >
          </v-img>
        </v-col>

        <v-col>
          <v-card flat class="d-flex flex-column fill-height">
            <v-card-title class="pt-0 px-0">
              {{ item[$localize("title")] }}
              <v-spacer></v-spacer>
            </v-card-title>
            <v-divider></v-divider>
            <v-card-text class="flex-grow-1">
              <div v-html="item[$localize('description')]"></div>
            </v-card-text>
            <v-divider></v-divider>

            <v-card-subtitle class="d-flex align-center">
              <v-spacer></v-spacer>
              <v-icon small class="mr-1">mdi-calendar</v-icon>
              {{ formatDate(item.created_at) }}
            </v-card-subtitle>
          </v-card>
        </v-col>
      </v-row>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  name: "FBlogDetail",
  props: {
    item: {
      type: Object,
      default: () => ({}),
    },
  },
  data: () => ({
    items: [
      {
        src: "https://picsum.photos/id/1/1920/1080",
      },
      {
        src: "https://picsum.photos/id/2/1920/1080",
      },
      {
        src: "https://picsum.photos/id/3/1920/1080",
      },
      {
        src: "https://picsum.photos/id/4/1920/1080",
      },
    ],
    slide: 0,
  }),
  methods: {
    formatDate(date) {
      return this.$dt
        .fromISO(date)
        .setLocale(this.$i18n.locale)
        .toLocaleString(this.$dt.DATE_MED);
    },
  },
};
</script>
