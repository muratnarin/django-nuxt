import kebabCase from "lodash/kebabCase";
export default {
  head: {
    titleTemplate: "%s - Django Nuxt",
    title: "Django Nuxt",
    htmlAttrs: {
      lang: "en",
    },
    meta: [
      { charset: "utf-8" },
      { name: "viewport", content: "width=device-width, initial-scale=1" },
      { hid: "description", name: "description", content: "" },
      { name: "format-detection", content: "telephone=no" },
    ],
    link: [{ rel: "icon", type: "image/x-icon", href: "/favicon.ico" }],
  },

  css: ["~/assets/custom.css"],

  plugins: [
    "~/plugins/vee-validate",
    "~/plugins/i18n",
    "~/plugins/dateTime",
    "~/plugins/gMap",
    "~/plugins/localizedString",
    "~/plugins/toast",
    "~/plugins/errorHandler",
  ],

  components: true,

  buildModules: ["@nuxtjs/eslint-module", "@nuxtjs/vuetify"],

  modules: [
    "@nuxtjs/axios",
    "@nuxtjs/auth-next",
    "@nuxtjs/i18n",
    "vue-sweetalert2/nuxt",
  ],

  axios: {
    proxy: true,
  },

  proxy: {
    "/api/": {
      target: "http://localhost:8000/",
      pathRewrite: { "^/api/": "" },
      changeOrigin: true,
      secure: false,
    },
  },

  auth: {
    redirect: {
      login: "/auth/login",
      logout: "/",
      callback: "/",
      home: "/",
    },
    strategies: {
      local: {
        scheme: "refresh",
        token: {
          property: "access",
          global: true,
        },
        refreshToken: {
          property: "refresh",
          data: "refresh",
        },
        user: {
          property: false,
          autoFetch: false,
        },
        endpoints: {
          login: {
            url: "/api/login/",
            method: "post",
          },
          refresh: {
            url: "/api/refresh-token/",
            method: "post",
          },
          logout: {
            url: "/api/revoke-token/",
            method: "post",
          },
          user: {
            url: "/api/currentuser/",
            method: "post",
          },
        },
      },
    },
  },

  vuetify: {
    customVariables: ["~/assets/variables.scss"],
    // optionsPath: "~/vuetify.options.js",
  },

  i18n: {
    strategy: "no_prefix",
    detectBrowserLanguage: {
      useCookie: true,
      cookieKey: "i18n_redirected",
      redirectOn: "root",
    },
    locales: [
      {
        code: "en",
        file: "en.js",
      },
      {
        code: "tr",
        file: "tr.js",
      },
    ],
    lazy: true,
    langDir: "lang/",
    defaultLocale: "tr",
    // onBeforeLanguageSwitch: (oldLocale, newLocale, isInitialSetup, context) => {
    //   const locale =
    //     context.i18n.locales.find((l) => l.iso === newLocale) || {};
    //   const isRTL = locale.dir === "rtl";
    //   if (isInitialSetup) {
    //     context.app.vuetify.preset.rtl = isRTL; // <--- makes vuetify direction work on initial page load
    //   }
    //   context.app.vuetify.framework.lang.current = locale.langCode;
    //   context.app.vuetify.framework.rtl = isRTL;
    // },
  },

  router: {
    middleware: ["auth"],
    extendRoutes(routes, resolve) {
      routes.forEach((route) => {
        if (!route.params) {
          route.path = route.path
            .split("/")
            .map((path) => {
              if (/^:/.test(path)) return path;
              return kebabCase(path);
            })
            .join("/");
        }
      });
    },
  },

  build: {
    transpile: ["vee-validate/dist/rules"],
  },
};
