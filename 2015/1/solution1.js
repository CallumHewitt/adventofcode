const tools = require('./tools')

const solve1 = () => {
    const input = tools.getInput(1)
    return result = input.split('')
        .map(characterToValue)
        .reduce((a, b) => a + b, 0)
}

const characterToValue = (character) => {
    return character === '(' ? 1 : -1
}

const solve2 = () => {
    const characters = tools.getInput(1).split('')
    let count = 0
    for (let [i, character] of characters.entries()) {
        if (count < 0) {
            return i;
        } else {
            count += characterToValue(character)
        }
    }
    throw new Error('Failed to go to the basement.')
}

console.log(solve1())
console.log(solve2())