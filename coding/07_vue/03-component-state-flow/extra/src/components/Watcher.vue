<template>
  <div>
    <!-- 1 -->
    <button @click="count++">Add 1</button>
    <p>Count: {{ count }}</p>

    <!-- 2 -->
    <input v-model="message">
    <p>Message length: {{ messageLength }}</p>
  </div>
</template>

<script setup>
  import { ref, watch } from 'vue'
  
  const count = ref(0)

  watch(count, (newValue, oldValue) => {
    console.log(`newValue: ${newValue}, oldValue: ${oldValue}`)
  })
  
  const message = ref('')
  const messageLength = ref(0)

  watch(message, (newValue) => {
    messageLength.value = newValue.length
  })

</script>

<style scoped>

</style>