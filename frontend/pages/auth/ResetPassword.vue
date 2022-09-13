<template>
  <v-row no-gutters justify="center" class="fill-height">
    <v-col md="6">
      <ValidationObserver ref="cForm" v-slot="{ handleSubmit }">
        <v-card flat class="mt-16">
          <v-card-title class="justify-center">
            <v-img src="/logo-red.png" contain max-width="150"></v-img>
          </v-card-title>
          <v-card-text class="pa-2">
            <div class="text-h4 text--primary font-weight-bold mb-5">
              {{ $t("button.changePassword") }}
            </div>

            <v-form>
              <label class="body-1">Otp</label>
              <c-otp
                v-model="credentials.token"
                length="6"
                outlined
                rules="required|min:6"
                name="label.email"
              ></c-otp>
              <c-text-field
                v-model="credentials.email"
                outlined
                rules="required"
                name="label.email"
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
                v-model="credentials.passwordConfirm"
                :append-icon="show2 ? 'mdi-eye' : 'mdi-eye-off'"
                rules="confirmed:password|required"
                :type="show2 ? 'text' : 'password'"
                outlined
                name="label.password_confirmation"
                autocomplete="new-password"
                @click:append="show2 = !show2"
              ></c-text-field>
            </v-form>
          </v-card-text>
          <v-card-actions>
            <v-btn
              block
              color="primary"
              large
              class="text-capitalize"
              @click="handleSubmit(submit)"
              >{{ $t("button.changePassword") }}</v-btn
            >
          </v-card-actions>

          <v-card-actions class="mb-5">
            <v-spacer></v-spacer>
            <v-btn
              left
              text
              min-width="0"
              height="0"
              color="primary"
              to="/auth/login"
              class="text-capitalize pa-0 mt-5"
              ><v-icon>mdi-arrow-left</v-icon
              >{{ $t("button.backToLogin") }}</v-btn
            >
            <v-spacer></v-spacer>
          </v-card-actions>
        </v-card>
      </ValidationObserver>
    </v-col>
  </v-row>
</template>

<script>
import CTextField from "~/components/form/CTextField";
import COtp from "~/components/form/COtp";
export default {
  name: "ResetPassword",
  auth: "guest",
  components: { COtp, CTextField },
  layout: "full",
  data: () => ({
    credentials: {},
    show: false,
    show2: false,
  }),
  methods: {
    async submit() {
      const success = await this.$refs.cForm.validate();
      if (success) {
        this.loading = true;
        try {
          await this.$axios.$post("/api/setpasswordwithtoken/", {
            ...this.credentials,
          });
          await this.$router.push("/auth/login");
        } catch (e) {
          this.$handleError(e);
        } finally {
          this.loading = false;
        }
      }
    },
  },
};
</script>
