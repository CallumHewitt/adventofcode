from utils import *

def solve(data):
    print("Solving...")
    return mapAndSum(calculateAdjustedFuel, data, True)

def calculateAdjustedFuel(mass):
    mass = int(mass)
    fuelRequired = calculateFuel(mass)
    nextFuel = calculateFuel(fuelRequired)
    while(nextFuel > 0):
        fuelRequired += nextFuel
        nextFuel = calculateFuel(nextFuel)
    return fuelRequired

def calculateFuel(mass):
    return (mass//3)-2

print(solve(getInputAsList(1)))