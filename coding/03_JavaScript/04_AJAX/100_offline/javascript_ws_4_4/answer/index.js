// index.js
const searchBtn = document.querySelector('.search-box__button')
const searchResult = document.querySelector('.search-result')

let page = 1 
let limit = 100


function fetchAlbums(page=1, limit=100) {
  const keyword = document.querySelector('.search-box__input').value
  // alert('브라우저에 확인!') // 테스트용 코드 

  if (!keyword.trim()) return
  
  // 아니라면 axios 요청
  const API_KEY = 'API_KEY'
  const BASE_URL = 'http://ws.audioscrobbler.com/2.0/'
  const searchUrl = `?method=album.search&format=json`
  const params = {
    api_key: API_KEY,
    album: keyword,
    page: page,
    limit: limit,
  }
  
  const requestUrl = BASE_URL + searchUrl
  axios({
    method: 'get',
    url: requestUrl,
    params,
  }).then(res => {
    const albums = res.data.results.albummatches.album

    albums.forEach(album => {
      const card = document.createElement('div')
      card.classList.add('search-result__card')
      
      const cardImg = document.createElement('img')
      cardImg.src = album.image[1]['#text']
      
      const cardText = document.createElement('div')
      cardText.classList.add('search-result__text')
      
      const cardArtistName = document.createElement('h2')
      cardArtistName.innerText = album.artist
      
      const cardAlbumName = document.createElement('p')
      cardAlbumName.innerText = album.name
      
      cardText.append(cardArtistName, cardAlbumName)
      card.append(cardImg, cardText)
      
      searchResult.appendChild(card)
    })
  }).catch(err => {
    alert('잠시 후 다시 시도해주세요.')
  })  
}

searchBtn.addEventListener('click', fetchAlbums)