export default function ({ app }) {
  app.vuetify.framework.lang.current = app.i18n.localeProperties.code;
  app.i18n.onLanguageSwitched = (ـ, newLocale) => {
    app.vuetify.framework.lang.current = newLocale;
  };
}
