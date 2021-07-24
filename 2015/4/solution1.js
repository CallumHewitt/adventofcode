const tools = require('./tools')
const md5 = require('md5')

const solve = (hashTester) => {
    const key = tools.getInput(1);
    let number = 1
    let hash = hashInputs(key, number)
    while(!(hashTester(hash))) {
        number++
        hash = hashInputs(key, number)
    }
    return number
}

const hashInputs = (key, number) => {
    return md5(key + number)
}

const testHashSolution1 = (hash) => {
    return hash.startsWith('00000')
}

const testHashSolution2 = (hash) => {
    return hash.startsWith('000000')
}

console.log(solve(testHashSolution1))
console.log(solve(testHashSolution2))