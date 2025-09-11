<template>
  <div>
    <button @click="count++">Add 1</button>
    <p>Count: {{ count }}</p>
    <p>{{ message }}</p>
  </div>
</template>

<script setup>
  import { ref, onMounted, onUpdated } from 'vue'
  
  onMounted(() => {
    console.log('mounted')
  })

  const count = ref(0)
  const message = ref(null)

  onUpdated(() => {
    message.value = 'updated!'
  })

</script>

<style scoped>

</style>