const tools = require('./tools')

const solve1 = () => {
    return tools.getInputList(1)
        .map(compartmentalise)
        .map(findInAll)
        .map(valueItem)
        .reduce((a, c) => a + c, 0)

}

const compartmentalise = (bag) => {
    return [ bag.slice(0, bag.length/2), bag.slice(bag.length/2) ]
}

const findInAll = (compartments) => {
    const intersection = intersect(compartments.map(x => x.split('')).map(x => new Set(x)))
    if (intersection.length == 0) {s
        throw 'No matching item found: ' + intersection
    }
    if (intersection.length > 1) {
        throw 'More than one matching item found: ' + intersection
    }
    return intersection[0]
}

const intersect = (sets) => {
    return sets.reduce((filtered, current) => {
        return [...filtered].filter(x => current.has(x))
    });
}

const valueItem = (char) => {
    if (char == char.toUpperCase()) {
        return char.charCodeAt() - 38
    } else {
        return char.charCodeAt() - 96
    }
}

const solve2 = () => {
    return partition(tools.getInputList(1), 3)
    .map(findInAll)
    .map(valueItem)
    .reduce((a, c) => a + c, 0)
}

const partition = (input, n) => {
    const output = []
    for (const [index, row] of input.entries()) {
        if (index % 3 == 0) {
            output.push([])
        }
        output[output.length - 1].push(row)
    }
    return output
}

console.log(solve1())
console.log(solve2())