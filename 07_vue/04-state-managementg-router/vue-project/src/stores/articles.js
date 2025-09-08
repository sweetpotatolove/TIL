import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useArticleStore = defineStore('article', () => {
  const article = ref([])

  return { article }
  // return { 
  //   'article': article 
  // }
})
