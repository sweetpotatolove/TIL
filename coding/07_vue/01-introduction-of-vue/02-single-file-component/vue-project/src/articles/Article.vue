<template>
  <div>
    {{ message }}
  </div>
</template>

<script setup>
  import { ref } from 'vue'
  const message = ref('hello')
</script>

<style scoped>

</style>