// store/accounts.js

import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import axios from 'axios'

export const useAccountStore = defineStore('account', () => {
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)
  const isLogin = computed(() => {
    return token.value ? true : false
  })
  const router = useRouter()

  const signUp = function (payload) {
    const username = payload.username
    const password1 = payload.password1
    const password2 = payload.password2
    const age = payload.age
    // const { username, password1, password2, age } = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        username: username,
        password1: password1,
        password2: password2,
        age: age,
      }
    })
    .then((res) => {
      console.log('회원가입 완료되었습니다.')
      const password = password1
      logIn({ username, password })
    })
    .catch((err) => console.log(err))
  }

  const logIn = function (payload) {
    const username = payload.username
    const password = payload.password
    // const { username, password } = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        username: username,
        password: password
      }
    })
    .then((res) => {
      // console.log('로그인 완료되었습니다.')
      // console.log(res.data) 
      token.value = res.data.key
      router.push({ name: 'ArticleView' })
    })
    .catch((err) => console.log(err))
  }

  const logOut = function () {
    axios({
      method: 'post',
      url: `${API_URL}/accounts/logout/`
    })
    .then((res) => {
      token.value = null
      router.push({ name: 'ArticleView' })
    })
    .catch((err) => {
      console.log(err)
    })
  }
    

  return { signUp, logIn, token, isLogin, logOut }
}, { persist: true })
