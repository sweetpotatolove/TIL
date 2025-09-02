<template>
  <div>
    <!-- [Bad] v-for with v-if -->
    <!-- <ul>
      <li v-for="todo in todos" v-if="!todo.isComplete" :key="todo.id">
        {{ todo.name }}
      </li>
    </ul> -->

    <!-- [Good] v-for with v-if (computed)-->
    <ul>
      <li v-for="todo in completeTodos" :key="todo.id">
        {{ todo.name }}
      </li>
    </ul>

    <!-- [Good] v-for with v-if -->
    <ul>
      <template v-for="todo in todos" :key="todo.id">
        <li v-if="!todo.isComplete">
          {{ todo.name }}
        </li>
      </template>
    </ul>
  </div>
</template>

<script setup>
  import { ref, computed } from 'vue'

  let id = 0

  const todos = ref([
    { id: id++, name: '복습', isComplete: true },
    { id: id++, name: '예습', isComplete: false },
    { id: id++, name: '저녁식사', isComplete: true },
    { id: id++, name: '노래방', isComplete: false }
  ])

  const completeTodos = computed(() => {
    return todos.value.filter((todo) => !todo.isComplete)
  })
</script>

<style scoped>

</style>