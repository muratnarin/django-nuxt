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
                {{ $t("label.login") }}
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
              <c-text-field
                v-model="password"
                :append-icon="show ? 'mdi-eye' : 'mdi-eye-off'"
                rules="required"
                :type="show ? 'text' : 'password'"
                outlined
                name="label.password"
                @click:append="show = !show"
              ></c-text-field>
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
              to="/auth/forgot-password"
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
import CTextField from "~/components/form/CTextField";
export default {
  name: "SignIn",
  auth: "guest",
  components: { CTextField },
  layout: "full",
  data: () => ({
    email: "",
    password: "",
    show: false,
    loading: false,
  }),
  methods: {
    async submit() {
      const success = await this.$refs.cForm.validate();
      if (success) {
        this.loading = true;
        try {
          await this.$auth.loginWith("local", {
            data: {
              email: this.email,
              password: this.password,
            },
          });
          await this.$auth.fetchUser();
          if (this.$auth.user.is_superuser) {
            await this.$router.push("/admin/users");
          } else {
            await this.$router.push("/");
          }
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
