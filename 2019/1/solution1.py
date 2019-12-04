from utils import *

def solve(data):
    print("Solving...")
    return mapAndSum(calculateFuel, data, True)

def calculateFuel(mass):
    return math.floor(int(mass)/3)-2

print(solve(getInputAsList(1)))