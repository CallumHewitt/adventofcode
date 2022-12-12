const tools = require('./tools')

const solve = (windowSize) => {
    const input = tools.getInput(1)
    return findMarkerIndex(input, windowSize)
}

const findMarkerIndex = (input, windowSize) => {
    marker = windowSize
    while (marker < input.length) {
        const buffer = input.slice(marker - windowSize, marker)
        if (isUnique(buffer)) {
            return marker
        }
        marker++
    }
    throw new 'Failed to find a marker.'
}

const isUnique = (str) => {
    return new Set(str.split('')).size == str.length
}

console.log('Q1: %s', solve(4))
console.log('Q1: %s', solve(14))