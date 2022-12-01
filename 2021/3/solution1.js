const tools = require('./tools')


const solve1 = () => {
    const binaries = getGammaAndEpsilonBinary(tools.getInputList(1))
    return parseInt(binaries.gamma, 2) * parseInt(binaries.epsilon, 2)
}

const getGammaAndEpsilonBinary = (input) => {
    const ones = Array(input[0].length).fill(0)
    const zeroes = Array(input[0].length).fill(0)
    input.forEach((string) => {
        string.split('').forEach((c, i) => {
            if (c === '0') {
                zeroes[i] += 1
            } else {
                ones[i] += 1
            }
        })
    })
    return {
        gamma: ones.map((value, i) => value >= zeroes[i] ? 1 : 0).join(''),
        epsilon: ones.map((value, i) => value >= zeroes[i] ? 0 : 1).join('')
    }
}

const solve2 = () => {
    const input = tools.getInputList(1)
    
    const o2 = calculateOxygenRating(input)
    const co2 = calculateCO2Rating(input)
    const lifeSupportRating = o2*co2
    console.log('Life support rating is %s', lifeSupportRating)
    return lifeSupportRating
}

const calculateOxygenRating = (input) => {
    return calculateRating(input, 'gamma', 'O2')
}

const calculateRating = (input, binaryName, logName) => {
    let potentialRatings = input
    let indexToCheck = 0
    while(potentialRatings.length > 1) {
        binaryRating = getGammaAndEpsilonBinary(potentialRatings)[binaryName]
        potentialRatings = potentialRatings
            .filter((measurement) => measurement[indexToCheck] == binaryRating[indexToCheck])
        indexToCheck++
    }
    const rating = potentialRatings[0]
    console.log('%s Rating is: %s', logName, rating)
    return parseInt(rating, 2)
}

const calculateCO2Rating = (input) => {
    return calculateRating(input, 'epsilon', 'CO2')
}

console.log(solve1())
console.log(solve2())