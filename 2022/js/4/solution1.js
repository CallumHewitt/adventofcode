const tools = require('./tools')

const solve1 = () => {
    return loadRanges()
        .filter(pair => containedWithin(pair[0], pair[1]) || containedWithin(pair[1], pair[0]))
        .length
}

const loadRanges = () => {
    return tools.getInputList(1)
        .map(input => input.split(','))
        .map(splitInput => splitInput.map(range => range.split('-').map(value => parseInt(value))))
}

const containedWithin = (elfInnerRange, elfOuterRange) => {
    return elfOuterRange[0] <= elfInnerRange[0] && elfOuterRange[1] >= elfInnerRange[1]
}

const solve2 = () => {
    return loadRanges()
        .filter(pair => overlap(pair[0], pair[1]))
        .length
}

const overlap = (elfRange1, elfRange2) => {
    return (elfRange1[0] <= elfRange2[0] && elfRange1[1] >= elfRange2[0]) ||
     (elfRange2[0] <= elfRange1[0] && elfRange2[1] >= elfRange1[0])
}

console.log(solve1())
console.log(solve2())