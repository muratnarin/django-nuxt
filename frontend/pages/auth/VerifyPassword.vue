<template>
  <v-row no-gutters justify="center" class="fill-height">
    <v-col md="5">
      <ValidationObserver ref="cForm" v-slot="{ handleSubmit }">
        <v-card flat class="mt-16">
          <v-card-title class="justify-center">
            <v-img src="/logo-red.png" contain max-width="150"></v-img>
          </v-card-title>
          <v-card-text class="pa-2">
            <div class="text-h4 text--primary font-weight-bold mb-2">
              {{ $t("button.verifyPasswordOtp") }}
            </div>

            <v-form>
              <c-otp
                v-model="email"
                length="6"
                outlined
                rules="required|min:6"
                name="label.email"
              ></c-otp>
            </v-form>
          </v-card-text>
          <v-card-actions class="mt-10">
            <v-spacer></v-spacer>
            {{ $t("label.receive_code") }}

            <v-btn
              text
              min-width="0"
              height="0"
              color="primary"
              class="text-capitalize pa-0"
              >{{ $t("button.resend") }}</v-btn
            >
            <v-spacer></v-spacer>
          </v-card-actions>

          <v-card-actions class="mt-16">
            <v-btn
              block
              color="primary"
              large
              class="text-capitalize"
              @click="handleSubmit(submit)"
              >{{ $t("button.reset_password") }}</v-btn
            >
          </v-card-actions>
          <v-card-actions class="mt-16">
            <v-spacer></v-spacer>
            <v-btn
              left
              text
              min-width="0"
              height="0"
              color="primary"
              to="/auth/forget-password"
              class="text-capitalize mt-16 pa-0"
              ><v-icon>mdi-arrow-left</v-icon
              >{{ $t("button.back_to_login") }}</v-btn
            >
            <v-spacer></v-spacer>
          </v-card-actions>
        </v-card>
      </ValidationObserver>
    </v-col>
  </v-row>
</template>

<script>
import COtp from "~/components/form/COtp";
export default {
  name: "VerifyPassword",
  auth: "guest",
  components: { COtp },
  layout: "full",
  data: () => ({
    email: "",
    password: "",
    show: false,
  }),
  methods: {
    async submit() {
      const success = await this.$refs.cForm.validate();
      if (success) {
        this.loading = true;
        try {
          await this.$axios.$post("/api/check-otp/", {
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
