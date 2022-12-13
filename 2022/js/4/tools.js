const fs = require('fs')

const getInput = (inputFileNumber) => {
    return fs.readFileSync(getInputFileName(inputFileNumber), 'utf-8')
}

const getInputCharacters = (inputFileNumber) => {
    return getInput(inputFileNumber).split('')
}

const getInputList = (inputFileNumber) => {
    return getInput(inputFileNumber).split(/\r?\n/)
}

const getInputListInts = (inputFileNumber) => {
    return getInputList(inputFileNumber).map((string) => parseInt(string, 10))
}

const getInputFileName = (inputFileNumber) => {
    return 'input' + inputFileNumber + '.txt'
}

const ifNanThenZero = (number) => {
    return number ? number : 0;
}

module.exports = {
    getInput,
    getInputCharacters,
    getInputList,
    getInputListInts,
    ifNanThenZero
}