export default ({ app, store }, inject) => {
  inject("toast", (content, type) => {
    store.commit("setMessage", { content, type });
  });
};
