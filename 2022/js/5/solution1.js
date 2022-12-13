const tools = require('./tools')

const solve = () => {
    const rows = tools.getInputList(1)
    const firstMoveIndex = rows.findIndex(element => element.startsWith('move'))
    const stacks = loadStacks(rows, firstMoveIndex)
    const instructions = rows.slice(firstMoveIndex);
    console.log('9000 Strategy (Q1): %s', topOfStacks(moveCrates(stacks, instructions, strategy9000)))
    console.log('9001 Strategy (Q2): %s', topOfStacks(moveCrates(stacks, instructions, strategy9001)))
}

const loadStacks = (rows, firstMoveIndex) => {
    const stackBottom = firstMoveIndex - 3
    const stacks = [];
    for(let i = 0; i < Math.ceil(rows[0].length/4); i++) {
        stacks.push([])
    }
    for (let row of rows.slice(0, stackBottom + 1).reverse()) {
        for (let [index, stack] of stacks.entries()) {
            const crate = row.charAt(1 + (index*4))
            if (crate != " ") {
                stack.push(crate)
            }
        }
    }
    return stacks
}

const moveCrates = (originalStacks, instructions, strategy) => {
    const regex = /move (\d+) from (\d+) to (\d+)/
    const stacks = originalStacks.map(stack => stack.slice())
    for (let instruction of instructions) {
        const groups = instruction.match(regex)
        const count = groups[1]
        const fromStack = groups[2] - 1
        const toStack = groups[3] - 1
        strategy(stacks, count, fromStack, toStack)
    }
    return stacks
}

const strategy9000 = (stacks, count, fromStack, toStack) => {
    for (let i = 0; i < count; i++) {
        const crate = stacks[fromStack].pop()
        stacks[toStack].push(crate)
    }
}

const strategy9001 = (stacks, count, fromStack, toStack) => {
    const crates = stacks[fromStack].splice(stacks[fromStack].length - count)
    stacks[toStack].push(...crates)
}

const topOfStacks = (stacks) => {
    return stacks.map(stack => stack[stack.length - 1]).join('')
}

solve()