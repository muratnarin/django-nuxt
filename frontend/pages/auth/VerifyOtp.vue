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
              {{ $t("button.verify") }}
            </div>
            <v-form>
              <ValidationObserver ref="cForm2">
                <c-text-field
                  v-model="credentials.email"
                  outlined
                  rules="required"
                  name="label.email"
                ></c-text-field>
              </ValidationObserver>

              <label class="body-1">Otp</label>
              <c-otp
                v-model="credentials.otp_code"
                length="6"
                outlined
                rules="required"
              ></c-otp>
            </v-form>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            {{ $t("label.receive_code") }}

            <v-btn
              text
              min-width="0"
              height="0"
              color="primary"
              class="text-capitalize pa-0 ml-1"
              @click="resend"
              >{{ $t("button.resend") }}</v-btn
            >
            <v-spacer></v-spacer>
          </v-card-actions>

          <v-card-actions class="mt-5">
            <v-btn
              block
              color="primary"
              large
              class="text-capitalize"
              @click="handleSubmit(submit)"
              >{{ $t("button.verify") }}</v-btn
            >
          </v-card-actions>
        </v-card>
      </ValidationObserver>
    </v-col>
  </v-row>
</template>

<script>
import COtp from "~/components/form/COtp";
import CTextField from "~/components/form/CTextField";
export default {
  name: "VerifyOtp",
  auth: "guest",
  components: { COtp, CTextField },
  layout: "full",
  data: () => ({
    credentials: {
      email: "",
      otp_code: "",
    },
    loading: false,
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
    async resend() {
      const success = await this.$refs.cForm2.validate();
      if (success) {
        this.loading = true;
        try {
          await this.$axios.$post("/api/send-otp-again/", {
            ...this.credentials,
          });
        } catch (e) {
          this.$handleError(e);
        }
      }
    },
  },
};
</script>
