<template>
  <div>
    <div v-for="(item, index) in myArr">
      {{ index }} / {{ item.name }}
    </div>
    <div v-for="(value, key, index) in myObj">
      {{ index }} / {{ key }} / {{ value }}
    </div>

    <!-- v-for on <template> -->
    <ul>
      <template v-for="item in myArr">
        <li>{{ item.name }}</li>
        <li>{{ item.age }}</li>
        <hr>
      </template>
    </ul>

    <!-- nested v-for -->
    <ul v-for="item in myInfo">
      <li v-for="friend in item.friends">
        {{ item.name }} - {{ friend }}
      </li>
    </ul>
  </div>
</template>

<script setup>
  import { ref } from 'vue'

  const myArr = ref([
    { name: 'Alice', age: 20 },
    { name: 'Bella', age: 21 }
  ])
  
  const myObj = ref({
    name: 'Cathy',
    age: 30
  })

  // nested v-for
  const myInfo = ref([
    { name: 'Alice', age: 20, friends: ['Bella', 'Cathy', 'Dan'] },
    { name: 'Bella', age: 21, friends: ['Alice', 'Cathy'] }
  ])
</script>

<style scoped>

</style>