import random


class Node:
    name = ''
    next_layer = []
    weights = []

    def __init__(self, name, next_layer, weights):
        self.name = name
        self.next_layer = next_layer
        if weights:
            self.weights = [random.uniform(0, 1)]*len(next_layer)
        else:
            self.weights = weights


