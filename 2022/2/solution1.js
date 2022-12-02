const tools = require('./tools')

const PLAYER_HANDS = ['X', 'Y', 'Z']
const ELF_HANDS = ['A', 'B', 'C']
const LOGS_ENABLED = true

const solve1 = () => {
    return runGame(playGame)
}

const runGame = (strategy) => {
    const input = tools.getInputList(1)
    return input.map((line) => {
        splitLine = line.split(/\s/)
        return strategy(splitLine[0], splitLine[1])
    }).reduce((a, n) => a + n)
}

const playGame = (elfHand, playerHand, ) => {
    log('======= Elf (%s) vs Player (%s) =======', elfHand, playerHand)
    const playerIndex = PLAYER_HANDS.indexOf(playerHand)
    const elfIndex = ELF_HANDS.indexOf(elfHand)

    let outcomeScore
    let diff = playerIndex - elfIndex
    if (diff == 1 || diff == -2) {
        log('Player wins! %s beats %s', playerHand, elfHand)
        outcomeScore = 6
    } else if (diff == 0) { 
        log('Draw! %s == %s', playerHand, elfHand)
        outcomeScore = 3
    } else {
        log('Elf wins! %s beats %s', elfHand, playerHand)
        outcomeScore = 0
    }
    return (playerIndex + 1) + outcomeScore
}

const log = (str, ...params) => {
    if (LOGS_ENABLED) {
        console.log(str, ...params)
    }
}

const solve2 = () => {
    return runGame(playGameStrategically)
}

const playGameStrategically = (elfHand, playerAim) => {
    const elfIndex = ELF_HANDS.indexOf(elfHand);
    log('\n')
    let playerHand
    if (playerAim == 'X') {
        log('Aiming to lose!')
        playerHand = PLAYER_HANDS[modWithNegativeSupport(elfIndex - 1, ELF_HANDS.length)]
    } else if (playerAim == 'Y') {
        log('Aiming to draw!')
        playerHand = PLAYER_HANDS[elfIndex]
    } else {
        log('Aiming to win!')
        playerHand = PLAYER_HANDS[(elfIndex + 1) % ELF_HANDS.length]
    }
    return playGame(elfHand, playerHand)    
}

const modWithNegativeSupport = (n, m) => {
    return ((n % m) + m) % m
}

console.log(solve1())
console.log(solve2())