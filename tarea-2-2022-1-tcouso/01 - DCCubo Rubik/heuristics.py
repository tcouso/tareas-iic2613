from cube import RCube 
from heuristics_utilities import corner_distances


def example_heuristic(state):
    '''Heurística de ejemplo, cuenta diferencias entre cubo inicial y final'''
    dif  = 0 
    for i in range(len(state)):
        if RCube.sol[i] != state[i]:
            dif += 1

    return dif


def max_manhattan_corners(state):
    '''
    Maximum of manhattan distances between a state corner's positions
    and a goal state corner's positions, divided by two.
    '''
    h = max(corner_distances(state)) / 2

    return h


def min_manhattan_corners(state):
    '''
    Minimum of manhattan distances between a state corner's positions
    and a goal state corner's positions, divided by two.
    '''
    h = min(corner_distances(state)) / 2

    return h


def sum_manhattan_corners(state):
    '''
    Sum of manhattan distances between a state corner's positions
    and a goal state corner's positions, divided by two.
    '''
    h = sum(corner_distances(state)) / 2

    return h

def max_steps_edges(state):
    """TODO"""
    pass


if __name__ == "__main__":

    state = "WGWWOOWOOOYYRYYWWRGBGOYYRWWGGRGBGYBOBYYRWRGOOGBBRRRBBB"

    print(max_manhattan_corners(state))
    print(min_manhattan_corners(state))
    print(sum_manhattan_corners(state))
