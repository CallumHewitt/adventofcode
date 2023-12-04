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

module.exports = {
    getInput,
    getInputCharacters,
    getInputList,
    getInputListInts,
    getInput2DArray,
    ifNanThenZero
}