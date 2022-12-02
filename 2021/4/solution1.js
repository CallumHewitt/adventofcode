const tools = require('./tools')

const solution = () => {
    const input = tools.getInputList(1)
    const numbers = input[0].split(',').map(x => parseInt(x))
    const boards = extractBoards(input)
    const winners = findWinners(numbers, boards)
    scoreWinner(winners[0], 'First winner')
    scoreWinner(winners[winners.length - 1], 'Last winner')
}

const scoreWinner = (winner, winnerName) => {
    const winnerUnmarkedSum = sumUnmarkedNumbers(winner.calledNumbers, winner.winningBoard)
    console.log('%s unmarked sum: %s', winnerName, winnerUnmarkedSum)
    console.log('%s score: %s', winnerName, winnerUnmarkedSum * winner.winningNumber)
}

const extractBoards = (input) => {
    const boardsInput = input.slice(2)
    const boards = [[]]
    boardsInput.forEach((row) => {
        if (row) {
            rowArray = row.split(/\s+/).filter(x => x != '').map(x => parseInt(x))
            boardId = boards.length - 1
            boards[boardId].push(rowArray)
        } else {
            boards.push([])
        }
    })
    return boards
}

const findWinners = (numbers, boards) => {
    const called = new Set()
    const winningBoards = new Set()
    const winners = []
    for (const number of numbers) {
        called.add(number)
        for (const board of boards) {
            if (winningBoards.has(board)) {
                continue
            }
            const potentialWinner = checkWinner(board, called)
            if (potentialWinner.length > 0) {
                winningBoards.add(board)
                winners.push({
                    calledNumbers: new Set(called),
                    winningNumber: number,
                    winningBoard: board,
                    winningLine: potentialWinner
                })
            }
        }
    }
    return winners
}

const checkWinner = (board, called) => {
    const horizontalWin = checkHorizontalWins(board, called)
    const verticalWin = checkVerticalWins(board, called)
    if (horizontalWin.length > 0) {
        return horizontalWin
    }
    if (verticalWin.length > 0) {
        return verticalWin
    }
    return []
}

const checkHorizontalWins = (board, called) => {
    for (const row of board) {
        if (allArrayValuesInSet(row, called)) {
            return row
        }
    }
    return []
}

const allArrayValuesInSet = (array, set) => {
    return array.reduce((a, n) => a && set.has(n), true)
}

const checkVerticalWins = (board, called) => {
    for (i = 0; i < board.length; i++) {
        verticalCandidate = board.map(row => row[i])
        if (allArrayValuesInSet(verticalCandidate, called)) {
            return verticalCandidate
        }
    }
    return []
}

const sumUnmarkedNumbers = (calledNumbers, winningBoard) => {
    return winningBoard.flatMap(n => n).filter(n => !calledNumbers.has(n)).reduce((a, n) => a + n)
}

solution()