const tools = require('./tools')

const solve1 = () => {
    const input = tools.getInputListInts(1)
    let increaseCount = 0;
    for (i = 1; i < input.length; i++) {
        if (input[i] > input[i-1]) {
            increaseCount++
        }
    }
    return increaseCount
}

const solve2 = () => {
    const input = tools.getInputListInts(1)
    let increaseCount = 0;
    for (i = 0; i < input.length - 2; i++) {
        if (windowSum(input, i) > windowSum(input, i-1)) {
            increaseCount++
        }
    }
    return increaseCount
}

const windowSum = (input, first) => {
    return input[first] + input[first + 1] + input[first + 2];
}

console.log(solve1())
console.log(solve2())