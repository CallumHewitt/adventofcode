const tools = require('./tools')

const NORTH = '^'
const EAST = '>'
const SOUTH = 'v'
const WEST = '<'

const solve1 = () => {
    const instructions = tools.getInputCharacters(1)
    return getVisitedHouses(instructions).size
}

const getVisitedHouses = (instructions) => {
    const houses = new Set();
    let x = 0
    let y = 0
    houses.add(toPointKey(x, y), 1)
    for (let step of instructions) {
        switch (step) {
            case NORTH:
                y++
                break;
            case EAST:
                x++;
                break;
            case SOUTH:
                y--;
                break;
            case WEST:
                x--;
                break;
        }
        houses.add(toPointKey(x, y))
    }
    return houses
}

const toPointKey = (x, y) => {
    return `${x},${y}`
}

const solve2 = () => {
    const instructions = tools.getInputCharacters(1)
    const instructions1 = instructions.filter((value, index) => index % 2 === 0)
    const instructions2 = instructions.filter((value, index) => index % 2 !== 0)
    const houses1 = getVisitedHouses(instructions1)
    const houses2 = getVisitedHouses(instructions2)
    return new Set([...houses1, ...houses2]).size
}

console.log(solve1())
console.log(solve2())