<template>
  <v-card>
    <v-card-text>
      <div class="d-flex align-center">
        <v-avatar size="120" class="mr-3">
          <img v-if="item.avatar" :src="item.avatar" alt="" />
          <v-icon v-else size="50">mdi-image</v-icon>
        </v-avatar>
        <div>
          <v-chip v-for="job in item.jobs" :key="job" small color="warning">
            {{ jobs.find((v) => v.id === job).name }}
          </v-chip>
          <div class="text-h6 mt-1">
            {{ item.fullName }}
          </div>
          <div class="subtitle-2">İstanbul, Turkey</div>
          <div class="d-flex mt-3">
            <div class="mr-5">
              <v-icon>mdi-email</v-icon>
              {{ item.email }}
            </div>
            <div>
              <v-icon>mdi-card-account-details</v-icon>
              {{ item.identity }}
            </div>
          </div>
          <div class="mt-2">
            <v-icon>mdi-phone</v-icon>
            {{ item.phone }}
          </div>
        </div>
        <v-spacer></v-spacer>
        <div class="align-self-start">
          Joined on {{ formatDate(item.updated_at) }}
        </div>
      </div>
    </v-card-text>
  </v-card>
</template>

<script>
import { DateTime } from "luxon";

export default {
  name: "UserDetails",
  props: {
    item: {
      type: Object,
      default: () => ({}),
    },
    jobs: {
      type: Array,
      default: () => [],
    },
  },
  methods: {
    formatDate(date) {
      return DateTime.fromISO(date)
        .setLocale(this.$i18n.locale)
        .toLocaleString(DateTime.DATE_MED);
    },
  },
};
</script>
