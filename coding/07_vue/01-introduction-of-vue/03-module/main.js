import { name, age, obj, some } from './sub.js'
import bob from './other.js'
import { newName } from './other.js'

console.log(name)
console.log(age)
console.log(some)
// console.log(privateValue)
obj.introduce()
console.log(bob)
console.log(newName)