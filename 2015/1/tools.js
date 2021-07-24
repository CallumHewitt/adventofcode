const fs = require('fs')

module.exports = {

    getInput: (inputFileNumber) => {
        return fs.readFileSync(getInputFileName(inputFileNumber), 'utf-8')
    }

}

const getInputFileName = (inputFileNumber) => {
    return 'input' + inputFileNumber + '.txt'
}