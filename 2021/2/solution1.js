const tools = require('./tools')

const solve = (pilotRoutine) => {
    const result = pilotRoutine()
    return result.x * result.y
}

const pilotSubmarine1 = () => {
    return getSteps()
        .reduce((position, step) => {
            const action = step.action
            const distance = step.distance
            if (action === 'forward') {
                position.x += distance
            } else if (action === 'up') {
                position.y = Math.max(0, position.y - distance)
            } else if (action === 'down') {
                position.y += distance
            }
            return position;
        }, { x: 0, y: 0, aim: 0 });
}

const getSteps = () => {
    return tools.getInputList(1)
        .map(step => step.match("(\\w*)\\s(\\d*)"))
        .map(match => { return { action: match[1], distance: parseInt(match[2]) }})
}

const pilotSubmarine2 = () => {
    return getSteps()
        .reduce((position, step) => {
            const action = step.action
            const distance = step.distance
            if (action === 'forward') {
                position.x += distance
                position.y = Math.max(0, position.y + (distance * position.aim))
            } else if (action === 'up') {
                position.aim -= distance
            } else if (action === 'down') {
                position.aim += distance
            }
            return position;
        }, { x: 0, y: 0, aim: 0 });
}

console.log(solve(pilotSubmarine1))
console.log(solve(pilotSubmarine2))