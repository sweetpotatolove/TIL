import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

// 여기는 article에 대한 처리를 관리하는 중앙 저장소
// 일반적으로 Back 서버에 요청을 보낼 엔드 포인트는?

const API_URL = 'http://127.0.0.1:8000/api/v1/articles'

export const useArticleStore = defineStore('article', () => {

  const articles = ref([
    {id: 1, title: 'title 1', content: 'content 1'}, 
    {id: 2, title: 'title 2', content: 'content 2'}, 
  ])

  // 게시글 상세 정보 조회가 필요 해지는 시점
  // ArticleView 컴포넌트가 Mount 되는 시점
  const getArticles = function () {
    axios({
      method: 'get',
      url: `${API_URL}/`
    })
      .then(res => {
        // console.log(res)
        articles.value = res.data
      })
      .catch(err => {
        console.log(err)
      })
  }

  return {
    articles,
    getArticles
  }
}, { persist: true })
