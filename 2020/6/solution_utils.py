import functools
import math

class Point:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'<{self.x}, {self.y}>'

    def __eq__(self, other):
        equal = False
        if isinstance(other, Point):
            equal = self.x == other.x and self.y == other.y
        return equal

    def __hash__(self):
        return hash((self.x, self.y))

    def manhattan_distance(self, p):
        return abs(self.x - p.x) + abs(self.y - p.y)

def mapAndSum(mapFunc, iterable, debug=False):
    result = -1
    mappedData = list(map(mapFunc, iterable))
    if (debug):
        print('Mapped data: ' + str(mappedData))
    return functools.reduce(lambda a,b: a + b, mappedData)