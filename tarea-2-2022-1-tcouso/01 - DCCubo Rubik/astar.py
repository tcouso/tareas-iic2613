import heuristics
import random
import time
import sys

from cube import RCube
from binary_heap import BinaryHeap
from node import Node


class Astar(object):
    def __init__(self, initial_state, heuristic = None):
        super(Astar, self).__init__()
        self.expansions = 0
        self.generated = 0
        self.cube = RCube(RCube.sol)
        self.cube_string = self.cube.flat_str()
        self.initial_state = initial_state
        self.heuristic = heuristic if heuristic else heuristics.example_heuristic
        self.open = BinaryHeap()
        self.closed_ = []

    def search(self):
        '''Implementar'''
        self.start_time = time.process_time()
        # instance initial state as node
        initial_node = Node(self.initial_state)

        # add initial state to open
        self.open.insert(initial_node)

        # set g(initial_node) to zero and h(initial_node) to heuristic value
        initial_node.g = 0
        initial_node.h = self.heuristic(initial_node.state)
    
        # set initial_node key as f(initial_node)
        initial_node.key = initial_node.g + initial_node.h

        # store initial state
        self.generated = {}
        self.generated[initial_node.state] = initial_node

        # start search
        while not self.open.is_empty():
            # extract node from open
            parent_node = self.open.extract()
            # check if extracted node is a goal state
            cube_s = RCube(parent_node.state)
            if cube_s.is_solved():
                # return solved cube node
                self.end_time = time.process_time()
                return (
                    parent_node.trace(), 
                    self.expansions, 
                    self.end_time - self.start_time
                    )
            # expand extracted node
            self.expansions += 1
            # extract successor states and moves
            for succ_state, move, cost in cube_s.succesors():
                # extract sucessor node
                child_node = self.generated.get(succ_state)
                is_new = child_node is None # child node generated for the first time
                path_cost = parent_node.g + cost # cost of arriving to child node

                if is_new or path_cost < child_node.g:
                    # add succ state to open if it is new or it has a better path
                    if is_new:
                        # instance new child node
                        child_node = Node(succ_state, parent_node)
                        child_node.h = self.heuristic(child_node.state)
                        self.generated[child_node.state] = child_node
                    # set child node  parameters
                    child_node.parent = parent_node
                    child_node.g = path_cost
                    # update child node f
                    child_node.key = child_node.g + child_node.h

                    # update open
                    self.open.insert(child_node)

        self.end_time = time.process_time()
        return None # leaf scenario



if __name__ == "__main__":
    cube = RCube(RCube.sol)
    print(cube.is_solved())
