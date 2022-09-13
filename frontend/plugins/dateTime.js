import { DateTime } from "luxon";
export default ({ app }, inject) => {
  inject("dt", DateTime);
};
