module.exports = {
  env: {
    browser: true,
    es2021: true,
  },
  extends: ["plugin:vue/essential", "@nuxtjs", "@vue/prettier"],
  parserOptions: {
    ecmaVersion: 12,
    parser: "@babel/eslint-parser",
    sourceType: "module",
    requireConfigFile: false,
  },
  plugins: ["vue"],
  rules: {
    "vue/multi-word-component-names": "off",
    "vue/valid-v-slot": "off",
    "no-console": "off",
    "no-unused-vars": "warn",
    "space-in-parens": "off",
    "computed-property-spacing": "off",
    "max-len": ["error", { code: 360 }],
    "prettier/prettier": [
      "error",
      {
        endOfLine: "auto",
      },
    ],
  },
};
