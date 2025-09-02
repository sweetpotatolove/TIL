const name = 'Alice'
const age = 23

const obj = {
  name,
  age,
  introduce() {
    console.log(`My Name is ${this.name}`)
    console.log(`and I am ${this.age} years old.`)
  }
}

export const some = '정의'
export { name, age, obj }
