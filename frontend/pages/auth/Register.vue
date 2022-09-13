<template>
  <v-row no-gutters justify="center" class="fill-height">
    <v-col md="6">
      <ValidationObserver ref="cForm" v-slot="{ handleSubmit }">
        <v-card flat class="mt-16">
          <v-card-title class="justify-center">
            <v-img src="/logo-red.png" contain max-width="150"></v-img>
          </v-card-title>
          <v-card-text class="pa-2">
            <div class="text-h4 text--primary font-weight-bold mb-2">
              {{ $t("button.register") }}
            </div>
            <div class="subtitle-2 mb-10">
              Lorem ipsum dolor sit amet, consectetur. <br />
              Pharetra nibh eget vulputate interdum libero.
            </div>

            <v-form autocomplete="new-password">
              <input type="text" name="email" class="d-none" />
              <input type="password" name="password" class="d-none" />
              <c-text-field
                v-model="credentials.email"
                outlined
                rules="required"
                name="label.email"
              ></c-text-field>
              <c-text-field
                v-model="credentials.first_name"
                outlined
                rules="required"
                name="label.first_name"
              ></c-text-field>
              <c-text-field
                v-model="credentials.last_name"
                outlined
                rules="required"
                name="label.last_name"
              ></c-text-field>
              <c-text-field
                v-model="credentials.password"
                :append-icon="show ? 'mdi-eye' : 'mdi-eye-off'"
                rules="required"
                :type="show ? 'text' : 'password'"
                outlined
                name="label.password"
                vid="password"
                @click:append="show = !show"
              ></c-text-field>
              <c-text-field
                v-model="credentials.repassword"
                :append-icon="show2 ? 'mdi-eye' : 'mdi-eye-off'"
                rules="confirmed:password|required"
                :type="show2 ? 'text' : 'password'"
                outlined
                name="label.password_confirmation"
                @click:append="show2 = !show2"
              ></c-text-field>
              <div class="d-flex align-center">
                <c-check-box
                  v-model="agreement"
                  :rules="{ required: { allowFalse: false } }"
                  name="label.terms_conditions"
                >
                  <template #label>
                    <i18n
                      tag="span"
                      class="subtitle-2 d-flex align-center"
                      path="label.terms_conditions_text"
                    >
                      <template #terms>
                        <v-btn
                          text
                          class="agree-link pa-0 text-capitalize primary--text subtitle-2 mx-1"
                          min-width="0"
                          height="0"
                          @click.stop="openDialog(1)"
                        >
                          {{ $t("label.terms") }}
                        </v-btn>
                      </template>
                      <template #privacy_policy>
                        <v-btn
                          text
                          class="agree-link pa-0 text-capitalize primary--text subtitle-2 mx-1"
                          min-width="0"
                          height="0"
                          @click.stop="openDialog(2)"
                        >
                          {{ $t("label.privacy_policy") }}
                        </v-btn>
                      </template>
                      <template #user_agreement>
                        <v-btn
                          text
                          class="agree-link pa-0 text-capitalize primary--text subtitle-2 mx-1"
                          min-width="0"
                          height="0"
                          @click.stop="openDialog(3)"
                        >
                          {{ $t("label.user_agreement") }}
                        </v-btn>
                      </template>
                    </i18n>
                  </template>
                </c-check-box>
              </div>
            </v-form>
          </v-card-text>
          <v-card-actions>
            <v-btn
              :loading="loading"
              block
              color="primary"
              large
              class="text-capitalize"
              @click="handleSubmit(submit)"
              >{{ $t("button.register") }}</v-btn
            >
          </v-card-actions>

          <v-card-actions class="mt-5 mb-10">
            <v-spacer></v-spacer>
            {{ $t("button.accountAlready") }}
            <v-btn
              text
              min-width="0"
              height="0"
              color="primary"
              to="/auth/login"
              class="agree-link pa-0 text-capitalize ml-1"
            >
              {{ $t("button.login") }}</v-btn
            >
            <v-spacer></v-spacer>
          </v-card-actions>
        </v-card>
      </ValidationObserver>
      <v-dialog :key="dialogKey" v-model="dialog" width="500">
        <v-card max-height="80vh" class="d-flex flex-column">
          <v-toolbar color="primary" dark>
            <v-toolbar-title> {{ dialogTitle }}</v-toolbar-title>
          </v-toolbar>
          <v-card-text class="flex-grow-0 overflow-y-auto pt-5">
            <div class="subtitle-2 mb-10">
              Lorem ipsum dolor sit amet, consectetur. <br />
              Pharetra nibh eget vulputate interdum libero.
            </div>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="primary" text @click="dialog = false">
              {{ $t("button.close") }}
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-col>
  </v-row>
</template>

<script>
import CTextField from "~/components/form/CTextField";
import CCheckBox from "~/components/form/CCheckBox";
export default {
  name: "SignUp",
  auth: "guest",
  components: { CCheckBox, CTextField },
  layout: "full",
  data: () => ({
    credentials: {
      email: "",
      name: "",
      lastname: "",
      password: "",
      repassword: "",
    },
    loading: false,
    agreement: false,
    show: false,
    show2: false,
    dialog: false,
    dialogKey: 0,
    dialogType: 1,
    dialogContent:
      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut " +
      "labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut " +
      "aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum " +
      "dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
  }),
  computed: {
    dialogTitle() {
      switch (this.dialogType) {
        case 1:
          return this.$t("label.terms");
        case 2:
          return this.$t("label.privacy_policy");
        case 3:
          return this.$t("label.user_agreement");
        default:
          return "";
      }
    },
  },
  methods: {
    async submit() {
      const success = await this.$refs.cForm.validate();
      if (success) {
        this.loading = true;
        try {
          await this.$axios.$post("/api/register/", {
            ...this.credentials,
          });
          await this.$router.push("/auth/verify-otp");
        } catch (e) {
          this.$handleError(e);
        } finally {
          this.loading = false;
        }
      }
    },
    openDialog(type) {
      this.dialogKey++;
      this.dialogType = type;
      this.dialog = true;
    },
  },
};
</script>
<style scoped>
.agree-link {
  text-decoration: none;
}
</style>
