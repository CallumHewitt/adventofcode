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

const getInputFileName = (inputFileNumber) => {
    return 'input' + inputFileNumber + '.txt'
}

module.exports = {
    getInput,
    getInputCharacters,
    getInputList
}