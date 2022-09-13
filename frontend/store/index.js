export const state = () => ({
  message: {},
  mini: false,
  menuStyle: {
    dark: false,
    color: "undefined",
    flat: false,
  },
  drawer: false,
});

export const mutations = {
  setMessage(state, payload) {
    state.message = payload;
  },
  setMini(state) {
    state.mini = !state.mini;
  },
  setMenuStyle(state, payload) {
    state.menuStyle = payload;
  },
  setDrawer(state, payload) {
    state.drawer = payload;
  },
};
