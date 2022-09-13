<template>
  <v-row no-gutters justify="center" class="fill-height mt-10">
    <v-col md="6" lg="4">
      <ValidationObserver ref="cForm" v-slot="{ handleSubmit }">
        <v-card flat class="mt-16">
          <v-form @submit.prevent="handleSubmit(submit)">
            <v-card-title class="justify-center">
              <v-img src="/logo-red.png" contain max-width="150"></v-img>
            </v-card-title>
            <v-card-text class="pa-2">
              <div class="text-h4 text--primary font-weight-bold mb-2">
                {{ $t("button.forgotPassword") }}
              </div>
              <div class="subtitle-2 mb-10">
                Lorem ipsum dolor sit amet, consectetur. <br />
                Pharetra nibh eget vulputate interdum libero.
              </div>

              <c-text-field
                v-model="email"
                outlined
                rules="required"
                name="label.email"
              ></c-text-field>
            </v-card-text>
            <v-card-actions>
              <v-btn
                block
                color="primary"
                large
                class="text-capitalize"
                @click="handleSubmit(submit)"
                >{{ $t("button.submit") }}</v-btn
              >
            </v-card-actions>

            <v-card-actions class="mt-5">
              <v-spacer></v-spacer>
              <v-btn
                left
                text
                min-width="0"
                height="0"
                color="primary"
                to="/auth/login"
                class="text-capitalize mt-5 pa-0"
                ><v-icon>mdi-arrow-left</v-icon
                >{{ $t("button.backToLogin") }}</v-btn
              >
              <v-spacer></v-spacer>
            </v-card-actions>
          </v-form>
        </v-card>
      </ValidationObserver>
    </v-col>
  </v-row>
</template>

<script>
import CTextField from "~/components/form/CTextField";
export default {
  name: "ForgotPassword",
  auth: "guest",
  components: { CTextField },
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
          await this.$axios.$post("/api/sendresetpasswordlink/", {
            email: this.email,
          });
          await this.$router.push("/auth/reset-password");
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
