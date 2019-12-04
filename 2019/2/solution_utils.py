import functools
import math

def mapAndSum(mapFunc, iterable, debug=False):
    result = -1
    mappedData = list(map(mapFunc, iterable))
    if (debug):
        print('Mapped data: ' + str(mappedData))
    return functools.reduce(lambda a,b: a + b, mappedData)