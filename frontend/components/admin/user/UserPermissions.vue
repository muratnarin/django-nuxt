<template>
  <v-card flat outlined :class="{ 'mt-5': index > 0 }">
    <v-card-title class="d-flex align-center">
      {{ `${index + 1}. ${permissionGroup.text}` }}
      <v-spacer></v-spacer>
      <span class="subtitle-1">Allow All</span>
      <v-checkbox
        class="mr-4 ml-2"
        :value="permissionGroup.selected"
        color="deep-purple accent-4"
        @click.native.stop="selectAll(permissionGroup)"
      ></v-checkbox>
    </v-card-title>
    <v-card-text>
      <v-list shaped dense>
        <v-list-item
          v-for="(permission, j) in permissionGroup.subItems"
          :key="`permission-${j}`"
        >
          <v-list-item-content>
            <v-list-item-title
              v-text="`${index + 1}.${j + 1} ${permission.text}`"
            ></v-list-item-title>
          </v-list-item-content>
          <v-list-item-content>
            <div class="d-flex align-center flex-grow-1">
              <div
                :class="{
                  'deep-purple--text font-weight-bold': !permission.override,
                }"
              >
                Inherit
              </div>

              <v-switch
                v-model="permission.override"
                color="deep-purple accent-4"
                class="ml-3 mt-0 pt-0"
                hide-details
                dense
                inset
              ></v-switch>
              <div
                :class="{
                  'deep-purple--text font-weight-bold': permission.override,
                }"
              >
                Override
              </div>
            </div>
          </v-list-item-content>
          <v-list-item-action>
            <v-checkbox
              v-model="permission.value"
              color="deep-purple accent-4"
              hide-details
              @change="checkAll(permissionGroup)"
            ></v-checkbox>
          </v-list-item-action>
        </v-list-item>
      </v-list>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  name: "UserPermissions",
  props: {
    permissionGroup: {
      type: Object,
      default: () => ({}),
    },
    index: {
      type: Number,
      required: true,
    },
  },
  methods: {
    selectAll(group) {
      const val = !!group.subItems.some((item) => !item.value);
      group.subItems.forEach((item) => {
        item.value = val;
      });
      group.selected = val;
    },
    checkAll(group) {
      group.selected = !!group.subItems.every((item) => item.value);
    },
  },
};
</script>

<style scoped></style>
