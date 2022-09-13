export const state = () => ({
  type: "",
  country: "",
  city: "",
  price_range: [1000, 5000],
  search: "",
});

export const mutations = {
  setType(state, payload) {
    state.type = payload;
  },
  setCountry(state, payload) {
    state.country = payload;
  },
  setCity(state, payload) {
    state.city = payload;
  },
  setPriceRange(state, payload) {
    state.price_range = payload;
  },
  setSearch(state, payload) {
    state.search = payload;
  },
};
