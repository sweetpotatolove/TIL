<template>
  <div>
    <p>{{ counterStore.count }}</p>
    <p>{{ counterStore.doubleCount }}</p>
    <button @click="onClick">+</button>
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'
const counterStore = useCounterStore()
console.log(counterStore)
const onClick = function () {
  counterStore.increment()
}
// counterStore.count + 1
</script>

<style scoped>

</style>