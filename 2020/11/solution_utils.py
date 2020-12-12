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

# Kahn's algorithm: https://en.wikipedia.org/wiki/Topological_sorting#Kahn's_algorithm
def topological_sort(start, graph):
    parentless_nodes = [start]
    sorted_nodes = []

    print(graph)
    while(parentless_nodes):
        pick = parentless_nodes.pop()
        sorted_nodes.append(pick)
        children = graph[pick][:]
        print(pick)
        print(children)
        for child in children:
            graph[pick].remove(child)
            parentless = True
            remaining_children = set(itertools.chain.from_iterable(graph.values()))
            if (child not in remaining_children):
                parentless_nodes.append(child)

    return sorted_nodes