export default ({ app, store }, inject) => {
  inject("localize", (key) => {
    return `${key}_${app.i18n.locale}`;
  });
};
