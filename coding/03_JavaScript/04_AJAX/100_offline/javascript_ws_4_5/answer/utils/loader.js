/*
 아래 코드는 수정하지 않습니다.
*/

const loader = `
  <div class="search-result--loading-card">
    <div class="search-result--loading-img"></div>
    <div class="search-result--loading-text">
      <h2 class="search-result--loading-artistName"></h2>
      <p class="search-result--loading-albumName"></p>
    </div>
  </div>
`
const loaderCnt = 5
const loaderList = []
for (let i = 0; i < loaderCnt; i++) {
  loaderList.push(loader)
}

const loadingList = document.querySelector('.search-result--loadingList')
loadingList.innerHTML += loaderList.join('')