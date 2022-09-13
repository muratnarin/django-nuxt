<template>
  <v-card flat color="transparent" rounded>
    <v-card-title class="justify-center pb-0">
      <v-icon x-large :color="item.icon_color">{{ item.icon }}</v-icon>
    </v-card-title>
    <v-card-title class="justify-center">
      {{ item[$localize("title")] }}
    </v-card-title>
    <v-card-text>
      <p>{{ item[$localize("summary")] }}</p>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  name: "FServiceCard",
  props: {
    item: {
      type: Object,
      default: () => ({}),
    },
  },
};
</script>
