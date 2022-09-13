<template>
  <v-row no-gutters justify="center" class="fill-height">
    <v-col md="6" lg="4">
      <ValidationObserver ref="cForm" v-slot="{ handleSubmit }">
        <v-card flat class="mt-16">
          <v-form @submit.prevent="handleSubmit(submit)">
            <v-card-text class="pa-2">
              <div class="text-h4 text--primary font-weight-bold mb-2">
                {{ $t("label.login") }}
              </div>
              <div class="subtitle-2 mb-10">
                Lorem ipsum dolor sit amet, consectetur. <br />
                Pharetra nibh eget vulputate interdum libero.
              </div>

              <c-text-field
                v-model="credentials.email"
                outlined
                rules="required"
                name="label.email"
              ></c-text-field>
              <label class="body-1">Otp</label>
              <c-otp
                v-model="credentials.otp_code"
                length="6"
                outlined
                rules="required"
              ></c-otp>
            </v-card-text>
            <v-card-actions>
              <v-btn
                block
                color="primary"
                large
                class="text-capitalize"
                type="submit"
                :loading="loading"
                >{{ $t("button.login") }}</v-btn
              >
            </v-card-actions>
          </v-form>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn
              text
              color="primary"
              to="/auth/forget-password"
              class="text-capitalize mb-10"
              >{{ $t("button.forgotPassword") }}</v-btn
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
import CTextField from "~/components/form/CTextField";
export default {
  name: "VerifyPasswordChange",
  components: { COtp, CTextField },
  layout: "guest",
  data: () => ({
    credentials: {
      email: "",
      otp_code: "",
    },
    loading: false,
  }),
  methods: {
    submit() {
      this.$router.push("/");
    },
  },
};
</script>
