import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

const API_URL = 'http://127.0.0.1:5000/api/v1/'

export const useCounterStore = defineStore('counter', () => {
  const count = ref(0)
  const doubleCount = computed(() => count.value * 2)
  
  function increment() {
    count.value++
  }

  return { count, doubleCount, increment }
}, { persist: true }
// {
//   persist: {
//     storage: sessionStorage
//   }
// }
)
