import capitalize from "lodash/capitalize";
export const crudMixin = {
  data: () => ({
    options: {},
    filterOptions: {},
    items: [],
    locales: [],
    itemId: null,
    editedIndex: -1,
    menu: false,
    total: null,
    loading: true,
    dialog: false,
    dialogKey: 0,
    deleteMessage: "this item",
  }),
  computed: {
    formTitle() {
      if (this.$i18n.locale === "en") {
        return this.editedIndex === -1
          ? "Add " + capitalize(this.$t(`label.${this.itemName}`))
          : "Edit " + capitalize(this.$t(`label.${this.itemName}`));
      } else {
        return this.editedIndex === -1
          ? capitalize(this.$t(`label.${this.itemName}`)) + " Ekle"
          : capitalize(this.$t(`label.${this.itemName}`)) + " Düzenle";
      }
    },
    localizedHeaders() {
      return this.headers.map((v) => ({
        ...v,
        text: this.$t(`label.${v.text}`),
        value: v.localize ? this.$localize(v.value) : v.value,
      }));
    },
  },
  watch: {
    options: {
      async handler() {
        await this.fetchItems();
      },
    },
  },
  methods: {
    addItem() {
      this.itemId = null;
      this.editedIndex = -1;
      this.dialogKey++;
      this.dialog = true;
    },
    editItem(item) {
      this.itemId = item.id;
      this.dialogKey++;
      this.editedIndex = 1;

      this.dialog = true;
    },
    closeDialog() {
      this.dialog = false;
      this.editedIndex = -1;
      this.dialogKey++;
    },
    async confirmDelete(id) {
      try {
        await this.$axios.$post(`/api/delete${this.itemName.toLowerCase()}/`, {
          id,
        });
        this.$toast("Successfully Deleted", 2);
        await this.fetchItems();
      } catch (e) {
        this.$handleError(e);
      }
    },
    async deleteItem(item) {
      if (
        await this.$refs.confirm.open(
          this.$i18n.locale === "en"
            ? `Are you sure you want to delete?`
            : `Silmek istediğinize emin misiniz?`
        )
      ) {
        await this.confirmDelete(item.id);
      }
    },

    async fetchItems() {
      try {
        this.loading = true;
        const { result, total } = await this.$axios.$post(
          `/api/get${this.itemName.toLowerCase()}s/`,
          { ...this.options }
        );
        this.items = result;
        this.total = total;
      } catch (e) {
        this.$handleError(e);
      } finally {
        this.loading = false;
      }
    },

    async save(item) {
      try {
        if (this.editedIndex === -1) {
          await this.$axios.$post(
            `/api/create${this.itemName.toLowerCase()}/`,
            item
          );
        } else {
          await this.$axios.$post(
            `/api/update${this.itemName.toLowerCase()}/`,
            item
          );
        }
        this.$toast("Successfully Saved", 2);
        this.closeDialog();
        await this.fetchItems();
        if (this.itemName === "user") {
          await this.$auth.fetchUser();
        }
      } catch (e) {
        this.$handleError(e);
      }
    },
  },
};
