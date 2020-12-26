import functools
import itertools
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
            remaining_children = set(
                itertools.chain.from_iterable(graph.values()))
            if (child not in remaining_children):
                parentless_nodes.append(child)

    return sorted_nodes


def manhattan_distance(start_x, start_y, end_x, end_y):
    return abs(start_x - end_x) + abs(start_y - end_y)


class LinkedNode:

    def __init__(self, value=None, prev=None, next=None):
        self.value = value
        self.next = next
        self.prev = prev

    def __repr__(self):
        return f'<value: {self.value}, prev_val: {self.prev.value if self.prev else None}, next_val: {self.next.value if self.next else None}>'


class HashedLinkedList:

    def __init__(self, lst, circular=False, debug_mode=False):
        start = LinkedNode(lst[0], None, None)
        self.start = start
        self.index = {start.value: start}
        self.debug_mode = debug_mode
        node = start
        for item in lst[1:]:
            if (debug_mode and item in self.index):
                raise ValueError(
                    'All items in a HashedLinkedList must have unique values.')
            new_node = LinkedNode(item, node, None)
            node.next = new_node
            self.index[item] = new_node
            node = new_node
        if circular:
            node.next = start
            start.prev = node

    def to_list(self):
        lst = []
        lst.append(self.start.value)
        node = self.start.next
        while(not (node == self.start or node == None)):
            lst.append(node.value)
            node = node.next
        return lst

    def get_node(self, value):
        return self.index[value] if value in self.index and not (self.index[value].next == None and self.index[value].prev == None) else None

    def len(self):
        return len(self.index)

    def extract(self, from_value, count):
        extract = []
        from_node = self.index[from_value]
        node = from_node
        for i in range(count):
            if (node == None):
                raise ValueError(
                    f'Ran out of linked list nodes to extract. from_value {from_value}, count {count}')

            if (node.prev):
                node.prev.next = node.next
            if (node.next):
                node.next.prev = node.prev

            if (node == self.start):
                self.start = node.next

            extract.append(node.value)
            next_node = node.next
            node.next = None
            node.prev = None
            node = next_node
        return extract

    def reinsert(self, after_value, lst):
        # reinserting means no need to add a new record to the index. Avoids a O(n) call when not in debug_mode.
        start = self.index[after_value]
        end = start.next
        last_node = start
        node = None
        for item in lst:
            if (self.debug_mode and item not in self.index):
                raise ValueError(f'Value {item} does not already exist in the HashedLinkedList')
            node = self.index[item]
            node.prev = last_node
            last_node.next = node
            last_node = node
        node.next = end
        end.prev = node

    def insert(self, after_value, lst):
        start = self.index[after_value]
        end = start.next
        last_node = start
        node = None
        for item in lst:
            if (self.debug_mode and item in self.index):
                raise ValueError(f'Cannot insert value {item} as it already exists in the HashedLinkedList')
            node = LinkedNode(item, last_node, None)
            self.index[item] = node
            last_node.next = node
            last_node = node
        node.next = end
        end.prev = node
