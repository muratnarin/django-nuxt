<template>
  <v-snackbar
    v-model="show"
    :top="message.type !== 1"
    :centered="message.type === 4 || message.type === 5"
    :color="handleColor"
    :timeout="message.type === 2 ? 1500 : 2500"
    @
    min-width="50px"
  >
    <div class="d-flex justify-space-between align-center">
      <template v-if="message.type === 4">
        <v-progress-circular indeterminate class="mr-3"></v-progress-circular>
        <div>{{ message.content }}</div>
      </template>
      <template v-else>
        <v-icon class="mr-2">mdi-{{ handleIcon }}</v-icon>
        <div>{{ message.content }}</div>
      </template>
    </div>
  </v-snackbar>
</template>

<script>
export default {
  name: 'CToast',
  data() {
    return {
      show: false,
      message: {},
    }
  },
  computed: {
    handleColor() {
      switch (this.message.type) {
        case 0:
          return 'info'
        case 1:
          return 'error'
        case 2:
          return 'success'
        case 3:
          return 'warning'
        case 4:
          return 'cyan'
        case 5:
          return 'warning'
        default:
          return 'info'
      }
    },
    handleIcon() {
      switch (this.message.type) {
        case 0:
          return 'information'
        case 1:
          return 'alert'
        case 2:
          return 'check-circle-outline'
        case 3:
          return 'alert'
        case 4:
          return 'information'
        case 5:
          return 'information'
        default:
          return 'information'
      }
    },
  },

  created() {
    this.$store.subscribe((mutation, state) => {
      if (mutation.type === 'setMessage') {
        this.message = { ...state.message }
        this.show = true
      }
    })
  },
}
</script>
<style>
::v-deep .v-snack__wrapper {
  min-width: 100px;
}
</style>
