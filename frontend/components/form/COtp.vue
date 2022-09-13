<template>
  <ValidationProvider
    v-slot="{ errors, valid, dirty }"
    :vid="$attrs.vid"
    :name="$attrs.vName || $attrs.name || $attrs.label"
    :mode="$attrs.mode || 'eager'"
    :rules="rules"
  >
    <v-otp-input
      v-model="innerValue"
      :error-messages="errors"
      :success="valid && dirty"
      v-bind="$attrs"
      :label="$t($attrs.label || $attrs.name)"
      autocomplete="do-no-autofill-this-one"
      v-on="$listeners"
    >
      <!-- pass through scoped slots -->
      <template
        v-for="(_, scopedSlotName) in $scopedSlots"
        #[scopedSlotName]="slotData"
      >
        <slot :name="scopedSlotName" v-bind="slotData" />
      </template>

      <!-- pass through normal slots -->
      <template v-for="(_, slotName) in $slots" #[slotName]>
        <slot :name="slotName" />
      </template>
    </v-otp-input>
  </ValidationProvider>
</template>

<script>
import { ValidationProvider } from "vee-validate";

export default {
  name: "COtp",
  components: {
    ValidationProvider,
  },
  props: {
    rules: {
      type: [Object, String],
      default: "",
    },
    value: {
      type: null,
      default: "",
    },
  },
  data: () => ({
    innerValue: "",
  }),
  watch: {
    // Handles internal model changes.
    innerValue(newVal) {
      this.$emit("input", newVal);
    },
    // Handles external model changes.
    value(newVal) {
      this.innerValue = newVal;
    },
  },
  created() {
    if (this.value) {
      this.innerValue = this.value;
    }
  },
};
</script>
