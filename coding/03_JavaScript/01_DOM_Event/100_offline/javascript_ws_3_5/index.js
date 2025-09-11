const scissorsButton = document.getElementById('scissors-button')
const rockButton = document.getElementById('rock-button')
const paperButton = document.getElementById('paper-button')
const modal = document.querySelector('.modal')
const modalContent = document.querySelector('.modal-content')

// 모달을 클릭하면 모달을 숨기는 이벤트 리스너를 추가한다.
modal.addEventListener('click', event => {
  modal.style.display = 'none'
})

// 플레이어 1과 플레이어 2의 승리 횟수를 초기화한다.
let count1 = 0
let count2 = 0

// 게임 로직을 처리하는 함수를 정의한다.
const playGame = (player1, player2) => {
  if (player1 === 'scissors') {
    if (player2 === 'rock') {
      count2 += 1
      return 2
    } else if (player2 === 'paper') {
      count1 += 1
      return 1
    } 
  } else if (player1 === 'rock') {
    if (player2 === 'scissors') {
      count1 += 1
      return 1
    } else if (player2 === 'paper') {
      count2 += 1
      return 2
    }
  } else {
    if (player2 === 'rock') {
      count1 += 1
      return 1
    } else if (player2 === 'scissors') {
      count2 += 1
      return 2
    }
  }
  return 0
}

// 버튼 클릭 이벤트를 처리하는 함수를 정의한다.
const buttonClickHandler = choice => event => {
  // 가위, 바위, 보 버튼을 비활성화한다.
  scissorsButton.disabled = true
  rockButton.disabled = true
  paperButton.disabled = true

  // 가능한 선택지를 배열에 담는다.
  const cases = ['scissors', 'rock', 'paper']
  // 무작위 인덱스를 생성한다.
  const randomIndex = Math.floor(Math.random() * 3)
  
  // 게임 결과를 계산한다.
  const result = playGame(choice, cases[randomIndex])

  // 플레이어 1과 플레이어 2의 이미지를 가져온다.
  const player1Img = document.querySelector('#player1-img')
  const player2Img = document.querySelector('#player2-img')

  // 플레이어 1의 이미지를 설정한다.
  player1Img.src = `./img/${choice}.png`

  // 플레이어 2의 이미지를 변경하면서 회전 애니메이션을 구현한다.
  let i = randomIndex + 1
  const rotateImg = () => {
    i = (i + 1) % 3
    player2Img.src = `./img/${cases[i]}.png`
  }

  // 이미지 회전을 위한 타이머를 설정한다.
  const timerId = setInterval(rotateImg, 100)
  // 3초 후에 타이머를 멈추고 결과를 처리한다.
  setTimeout(() => {
    clearInterval(timerId)
    // 결과를 화면에 표시한다.
    const countA = document.querySelector('.countA')
    const countB = document.querySelector('.countB')
    countA.innerText = count1
    countB.innerText = count2
    player2Img.src = `./img/${cases[randomIndex]}.png`
    modalContent.innerText = result ? `Player ${result} wins!` : 'It\'s a tie!'
    modal.style.display = 'flex'
    // 버튼을 다시 활성화한다.
    scissorsButton.disabled = false
    rockButton.disabled = false
    paperButton.disabled = false
  }, 3000)
}

// 가위 버튼 클릭 이벤트에 대한 핸들러를 등록한다.
scissorsButton.addEventListener('click', buttonClickHandler('scissors'))
// 바위 버튼 클릭 이벤트에 대한 핸들러를 등록한다.
rockButton.addEventListener('click', buttonClickHandler('rock'))
// 보 버튼 클릭 이벤트에 대한 핸들러를 등록한다.
paperButton.addEventListener('click', buttonClickHandler('paper'))
