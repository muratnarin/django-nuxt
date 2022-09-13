<template>
  <v-carousel
    v-intersect="{
      handler: onIntersect,
      options: {
        rootMargin: '-48px',
      },
    }"
    :show-arrows="false"
    cycle
    hide-delimiters
    height="600"
  >
    <v-carousel-item
      v-for="(item, i) in items"
      :key="i"
      :src="item.src"
    ></v-carousel-item>
  </v-carousel>
</template>

<script>
export default {
  name: "FSlider",
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
      {
        src: "https://picsum.photos/id/5/1920/1080",
      },
    ],
  }),
  methods: {
    onIntersect(entries) {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          this.$store.commit("setMenuStyle", {
            dark: true,
            color: "rgba(0,0,0,.38)",
            flat: true,
          });
        } else {
          this.$store.commit("setMenuStyle", {
            dark: false,
            color: undefined,
            flat: false,
          });
        }
      });
    },
  },
};
</script>
