const tools = require('./tools')

const runLightCalc = (instructionProcessor) => {
    const lights = initializeLights(1000)
    const instructions = getInstructions()
    instructions.forEach(instruction => {
        processLights(lights, instruction, instructionProcessor)
    })
    return calculateLightBrightness(lights)
}

const initializeLights = (size) => {
    return new Array(size).fill(0).map(() => new Array(size).fill(0))
}

const getInstructions = () => {
    return tools.getInputList(1).map((instructionString) => {
        const match = instructionString.match("(.*)\\s{1}(\\d{1,3}),(\\d{1,3}) through (\\d{1,3}),(\\d{1,3})")
        return { action: match[1], x1: match[2], y1: match[3], x2: match[4], y2: match[5]}
    })
}

const processLights = (lights, instruction, instructionProcessor) => {
    const maxX = Math.max(instruction.x1, instruction.x2)
    const minX = Math.min(instruction.x1, instruction.x2)
    const maxY = Math.max(instruction.y1, instruction.y2)
    const minY = Math.min(instruction.y1, instruction.y2)
    for (x = minX; x <= maxX; x++) {
        for (y = minY; y <= maxY; y++) {
            instructionProcessor(lights, x, y, instruction.action)
        }
    }
}

const calculateLightBrightness = (lights) => {
    return lights.reduce((count, row) => count + row.reduce((innerCount, light) => innerCount + light, 0), 0)
}

const processInstruction1 = (lights, x, y, action) => {
    if (action == "toggle") {
        lights[x][y] = lights[x][y] == 0 ? 1 : 0
    } else if (action == "turn off") {
        lights[x][y] = 0
    } else if (action == "turn on") {
        lights[x][y] = 1
    }
}

const processInstruction2 = (lights, x, y, action) => {
    if (action == "toggle") {
        lights[x][y] = lights[x][y] + 2
    } else if (action == "turn off") {
        lights[x][y] = Math.max(lights[x][y] - 1, 0)
    } else if (action == "turn on") {
        lights[x][y] = lights[x][y] + 1
    }
}

console.log(runLightCalc(processInstruction1))
console.log(runLightCalc(processInstruction2))

