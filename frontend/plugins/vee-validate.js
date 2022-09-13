import Vue from "vue";
import {
  ValidationObserver,
  ValidationProvider,
  extend,
  configure,
} from "vee-validate";
import {
  required,
  confirmed,
  min,
  max,
  // eslint-disable-next-line camelcase
  alpha_dash,
} from "vee-validate/dist/rules";

// Add a rule.
extend("required", required);
extend("confirmed", confirmed);
extend("min", min);
extend("max", max);
extend("alpha_dash", alpha_dash);

// Register it globally
Vue.component("ValidationObserver", ValidationObserver);
Vue.component("ValidationProvider", ValidationProvider);

export default function VeeValidatePlugin({ app }) {
  configure({
    defaultMessage: (_, values) =>
      app.i18n.t(`validations.${values._rule_}`, values),
  });
}
