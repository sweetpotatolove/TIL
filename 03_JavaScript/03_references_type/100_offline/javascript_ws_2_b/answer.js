const person = {
  name: 'Alice',
  age: 30,
  city: 'New York',
  introduce: function () {
    return `안녕하세요 ${this.city}에 거주하는 ${this.age}살 ${this.name}입니다.`
  }
}