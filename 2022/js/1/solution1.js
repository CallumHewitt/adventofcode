const tools = require('./tools')

const solve = () => {
    const input = tools.getInputList(1)
    let currentCalories = 0
    let topCalories = [0,0,0]
    input.forEach(newCalorie => {
        if (newCalorie) {
            currentCalories += parseInt(newCalorie)
        } else {
            updateTopCalories(currentCalories, topCalories)
            currentCalories = 0
        }
    })
    console.log('Top calories: %s', topCalories)
    return topCalories.reduce((s,n) => s+n, 0)
}

const updateTopCalories = (currentCalories, topCalories) => {
    let minTopCalorie = Number.MAX_VALUE
    let minTopCalorieIndex = 0
    topCalories.forEach((topCalorie, index) => {
        if (topCalorie <= minTopCalorie) {
            minTopCalorie = topCalorie
            minTopCalorieIndex = index
        }
    })
    if (minTopCalorie < currentCalories) {
        topCalories[minTopCalorieIndex] = currentCalories
    }
    
}

console.log(solve())