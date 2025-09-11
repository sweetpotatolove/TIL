<template>
  <div>
    <!-- Binding to Objects -->
    <div :style="{ color: activeColor, fontSize: fontSize + 'px' }">Text</div>
    <div :style="{ 'font-size': fontSize + 'px' }">Text</div>
    <div :style="styleObj">Text</div>

    <!-- Binding to Arrays -->
    <div :style="[styleObj, styleObj2]">Text</div>
  </div>
</template>

<script setup>
  import { ref } from 'vue'

  const activeColor = ref('crimson')
  const fontSize = ref(50)

  const styleObj = ref({
    color: activeColor,
    fontSize: fontSize.value + 'px'
  })
  
  const styleObj2 = ref({
    color: 'blue',
    border: '1px solid black'
  })
</script>

<style scoped>

</style>