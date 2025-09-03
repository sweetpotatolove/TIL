<template>
  <section>
    <h1>Parent</h1>
    <ParentChild 
      my-msg="message"
      :my-balance="balance"
    />
    <ParentItem 
      v-for="info in children"
      :key="info.name"
      :my-info="info"
      @balance-update="onBalanceUpdate"
    />
  </section>
</template>

<script setup>
import ParentChild from './ParentChild.vue';
import ParentItem from './ParentItem.vue';
import { ref } from 'vue'

const balance = ref(10000)
const children = ref([
  {name: 'Alice', balance: 1000},
  {name: 'Bella', balance: 10000},
  {name: 'Chalie', balance: 100000},
])

const onBalanceUpdate = function (name) {
  // console.log('용돈 올려달라고? 너... 누구니?')
  // console.log(name)
  children.value.forEach(info => {
    if (info.name === name) {
      if (info.balance <= 5000) {
        info.balance += 1000
      } else {
        alert("너 이미 돈 충분히 있잖아!!!")
      }
      
    }
  })
}
</script>

<style scoped>

</style>