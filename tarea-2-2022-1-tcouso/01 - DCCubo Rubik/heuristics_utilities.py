from cube import RCube

def manhattan_distance(pos1, pos2):
    """
    Computes the manhattan distances between two rubik's cube pieces positions.
    """
    d = abs(pos2.x- pos1.x) + abs(pos2.y- pos1.y) + abs(pos2.z- pos1.z)

    return d

def goal_position(piece):
    """
    Returns the goal postion of a given piece.
    """
    goal_state = RCube(RCube.sol)
    goal_piece = goal_state.find_piece(*piece.colors)
    goal_pos = goal_piece.pos

    return goal_pos


def corner_distances(state):
    """
    Iterable of corner distances between state and goal state.
    """
    cube = RCube(state)
    for corner in cube.corners:
        goal_pos = goal_position(corner)
        corner_pos = corner.pos

        d = manhattan_distance(corner_pos, goal_pos)

        yield d

if __name__ == "__main__":
    cube = RCube(RCube.sol)
    for corner in cube.corners:
        print(type(corner))