const tools = require('./tools')

const solve1 = () => {
    const input = tools.getInputList(1)
    return input
        .map(parseDimensions)
        .map(dimensionsToRequiredWrapping)
        .reduce((a, b) => a + b, 0)
}

const parseDimensions = (row) => {
    const dimensions = row.split('x')
    return {
        l: parseInt(dimensions[0]),
        w: parseInt(dimensions[1]),
        h: parseInt(dimensions[2])
    }
}

const dimensionsToRequiredWrapping = (dimensions) => {
    const lw = dimensions.l * dimensions.w
    const wh = dimensions.w * dimensions.h
    const hl = dimensions.h * dimensions.l

    return 2 * lw + 2 * wh + 2 * hl + Math.min(lw, wh, hl)
}

const solve2 = () => {
    const input = tools.getInputList(1)
    return input
        .map(parseDimensions)
        .map(dimensionsToRequiredRibbon)
        .reduce((a, b) => a + b, 0)
}

const dimensionsToRequiredRibbon = (dimensions) => {
    const lwPerimeter = 2 * (dimensions.l + dimensions.w)
    const whPerimeter = 2 * (dimensions.w + dimensions.h)
    const hlPerimeter = 2 * (dimensions.h + dimensions.l)

    return Math.min(lwPerimeter, whPerimeter, hlPerimeter) + dimensionsToVolume(dimensions)
}

const dimensionsToVolume = (dimensions) => {
    return dimensions.l * dimensions.h * dimensions.w
}

console.log(solve1())
console.log(solve2())