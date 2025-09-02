<template>
  <div>
    <!-- if else -->
    <p v-if="isSeen">true일때 보여요</p>
    <p v-else>false일때 보여요</p>
    <button @click="isSeen = !isSeen">토글</button>

    <!-- else if -->
    <div v-if="name === 'Alice'">Alice입니다</div>
    <div v-else-if="name === 'Bella'">Bella입니다</div>
    <div v-else-if="name === 'Cathy'">Cathy입니다</div>
    <div v-else>아무도 아닙니다.</div>

    <!-- v-if on <template> -->
    <template v-if="name === 'Cathy'">
      <div>Cathy입니다</div>
      <div>나이는 30살입니다</div>
    </template>

    <!-- v-show -->
    <div v-show="isShow">v-show</div>
  </div>
</template>

<script setup>
  import { ref } from 'vue'

  const isSeen = ref(true)

  const name = ref('Cathy')
  
  const isShow = ref(false)
</script>

<style scoped>

</style>