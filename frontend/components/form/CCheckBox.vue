<template>
  <ValidationProvider
    v-slot="{ errors, valid, touched }"
    :vid="$attrs.vid"
    :name="$attrs.vName || $attrs.name || $attrs.label"
    :mode="$attrs.mode || 'eager'"
    :rules="rules"
  >
    <v-checkbox
      v-model="innerValue"
      :error-messages="errors"
      :success="valid && touched"
      v-bind="$attrs"
      :label="$t($attrs.label || $attrs.name)"
      :color="$vuetify.theme.dark ? 'grey' : 'primary'"
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
    </v-checkbox>
  </ValidationProvider>
</template>

<script>
import { ValidationProvider } from "vee-validate";

export default {
  name: "CCheckBox",
  components: {
    ValidationProvider,
  },
  props: {
    rules: {
      type: [Object, String],
      default: "",
    },
    // must be included in props
    value: {
      type: Boolean,
      default: null,
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
