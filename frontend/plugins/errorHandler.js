export default ({ app, store }, inject) => {
  inject("handleError", (error) => {
    let e = "Unexpected Error Occurred";
    if (error?.response?.data?.detail) {
      e = error.response.data.detail;
    }
    if (error?.response?.data?.message) {
      e = error.response.data.message;
    }
    if (error?.response?.data?.slug) {
      e = error.response.data.slug[0];
    }
    store.commit("setMessage", { content: e, type: 1 });
  });
};
