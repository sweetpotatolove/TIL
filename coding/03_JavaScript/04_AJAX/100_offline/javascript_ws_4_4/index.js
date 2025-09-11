// index.js

// 버튼에 함수 달기 위해 찝어오고, search-result 아래 DOM 추가될 것이므로 그 시작점을 찝어옴
const searchInput = document.querySelector('.search-box__button')
const searchResult = document.querySelector('.search-result')  

let page = 1 
let limit = 100
// 버튼에 fetchAlbums 함수를 달아줍니다.
searchInput.addEventListener('click', fetchAlbums)

// axios 요청 전 로더 띄우고 -> 요청 결과를 받아옴.
// html 만드는 역할은 다른 함수로 세분
async function fetchAlbums(page=1, limit=100) {
  // input 내용이 없다면 return
  const keyword = document.querySelector('.search-box__input').value
  if (!keyword.trim()) return
  
  // 아니라면 axios 요청
  const API_KEY = 'API key'
  const BASE_URL = 'http://ws.audioscrobbler.com/2.0/'
  const searchUrl = `?method=album.search&format=json`
  const params = {
    api_key: API_KEY,
    album: keyword,
    page: 1,
    limit: 100,
  }
  
  const requestUrl = BASE_URL + searchUrl
  const res = await axios.get(requestUrl, { params })
  console.log(res)
  // 앨범들 정보입니다.
  const albums = res.data.results.albummatches.album
  
  appendAlbumCards(albums)
}

// 요청 결과를 인자로 받아 html 만들고, 마지막에 sentinel 이동까지 담당
function appendAlbumCards(albums) {
  const cardList = document.createDocumentFragment() // Optimized Version
  albums.forEach(album => {  
    
    // left side's image tag
    const cardImg = document.createElement('img')
    cardImg.src = album.image[1]['#text']
    
    // right side content
    const cardArtistName = document.createElement('h2')
    const cardAlbumName = document.createElement('p')
    cardArtistName.innerText = album.artist
    cardAlbumName.innerText = album.name
    
    // right side box
    const cardText = document.createElement('div')
    cardText.classList.add('search-result__text')
    cardText.append(cardArtistName, cardAlbumName)
    
    // card (left + right)
    const card = document.createElement('div')
    card.classList.add('search-result__card')
    card.append(cardImg, cardText)
    // 앨범 클릭 시 js 로 redirect 하는 코드
    card.addEventListener('click', () => {
      window.location.href = album.url
    })
    // 카드리스트 안에 카드 마크업 + css 합본 전부 넣어주고,
    cardList.appendChild(card)
  })
  
  // 검색 결과 영역 아래 붙여줍니다.
  searchResult.append(cardList)
}
