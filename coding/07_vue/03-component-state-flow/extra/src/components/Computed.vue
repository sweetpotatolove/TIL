<template>
  <div>
    <h2>남은 할 일</h2>
    <p>{{ restOfTodos }}</p>
    <p>{{ restOfTodos }}</p>
    <p>{{ restOfTodos }}</p>
    <p>{{ getRestOfTodos() }}</p>
    <p>{{ getRestOfTodos() }}</p>
    <p>{{ getRestOfTodos() }}</p>
  </div>
</template>

<script setup>
  import { ref, computed } from 'vue'

  const todos = ref([
    { text: 'Vue 실습' },
    { text: '자격증 공부' },
    { text: 'TIL 작성' }
  ])

  const restOfTodos = computed(() => {
    console.log('computed')
    return todos.value.length > 0 ? '아직 남았다' : '퇴근!'
  })

  const getRestOfTodos = function () {
    console.log('method')
    return todos.value.length > 0 ? '아직 남았다' : '퇴근!'
  }

</script>

<style scoped>

</style>