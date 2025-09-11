<template>
  <div>
    <!-- Maintaining State with key -->
    <div v-for="item in items" :key="item.id">
      <p>{{ item.id }}</p>
      <p>{{ item.name }}</p>
    </div>
  </div>
</template>

<script setup>
  import { ref } from 'vue'

  let id = 0

  const items = ref([
    { id: id++, name: 'Alice' },
    { id: id++, name: 'Bella' },
  ])
</script>

<style scoped>

</style>