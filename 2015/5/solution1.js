const tools = require('./tools')

const solve1 = () => {
    const input = tools.getInputList(1)
    const niceStrings = input
        .filter(string => string.match("(.*[aeiou].*){3}")) // Contains 3 Vowels
        .filter(string => string.match("(.)\\1{1}")) // Contains same character sequentially
        .filter(string => !string.match("(ab|cd|pq|xy)")) // Does not contain any of these pairs
    return niceStrings
}

const solve2 = () => {
    const input = tools.getInputList(1)
    const niceStrings = input
        .filter(string => string.match("(.{2}).*\\1")) // Contains same pair of characters twice without overlaps
        .filter(string => string.match("(.)(.){1}\\1")) // Contains same character with single character between
    return niceStrings
}

console.log(solve1().length)
console.log(solve2().length)