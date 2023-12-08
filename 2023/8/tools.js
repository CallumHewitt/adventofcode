const fs = require('fs')


const getInput = (inputFileNumber) => {
    return fs.readFileSync(getInputFileName(inputFileNumber), 'utf-8')
}

const getInputFileName = (inputFileNumber) => {
    return 'input' + inputFileNumber + '.txt'
}

const getInputList = (inputFileNumber) => {
    return getInput(inputFileNumber).split(/\r?\n/)
}

const getInputCharacters = (inputFileNumber, includeLineBreaks=false) => {
    return getInput(inputFileNumber).split('').filter(x => x != '\n' && x != '\r')
}

const getInputListInts = (inputFileNumber) => {
    return getInputList(inputFileNumber).map((string) => parseInt(string, 10))
}

const getInput2DArray = (inputFileNumber, delimiter='') => {
    return getInputList(inputFileNumber).map(s => [...s.split(delimiter)])
}

const ifNanThenZero = (number) => {
    return number ? number : 0;
}

const greatestCommonDivisor = (a, b) => {
    return b == 0 ? a : greatestCommonDivisor (b, a % b)
}

const lowestCommonMultiple = (a, b) => {
    return a / greatestCommonDivisor (a, b) * b
}
const lowestCommonMultipleRange = (numbers) => {
    return numbers.reduce(lowestCommonMultiple, 1)
}

module.exports = {
    getInput,
    getInputCharacters,
    getInputList,
    getInputListInts,
    getInput2DArray,
    ifNanThenZero,
    lowestCommonMultiple,
    lowestCommonMultipleRange
}