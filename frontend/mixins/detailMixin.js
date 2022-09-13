export const detailMixin = {
  data: () => ({
    items: [],
    locales: [],
    itemId: {},
    editedIndex: -1,
    menu: false,
    totalItemsCount: null,
    loading: true,
    dialog: false,
    dialogKey: 0,
    deleteMessage: "this item",
  }),
  computed: {
    formTitle() {
      return this.editedIndex === -1
        ? "New " + this.itemName
        : "Edit " + this.itemName;
    },
  },
  methods: {
    editItem() {
      this.dialogKey++;
      this.editedIndex = 1;
      this.itemId = this.$route.params.id;
      this.dialog = true;
    },
    closeDialog() {
      this.dialog = false;
      this.editedIndex = -1;
      this.dialogKey++;
    },
    async save(item) {
      try {
        const submit = await this.$axios.$put(
          `/cms/${this.itemName.toLowerCase()}/${
            item instanceof FormData ? item.get("id") : item.id
          }/`,
          item
        );

        this.$toast("Successfully Saved", 2);
        this.closeDialog();
        await this.$fetch();
        await this.$auth.fetchUser();
      } catch (e) {
        this.$handleError(e);
      } finally {
        this.loading = false;
      }
    },
  },
};
