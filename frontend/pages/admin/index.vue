<template>
  <div></div>
</template>

<script>
export default {
  name: 'Index',
  middleware: [
    ({ redirect }) => {
      redirect('/dashboard')
    },
  ],
}
</script>

<style scoped></style>
