import random
from game import Connect4


# Implementation based on "check_win" method of "Connect4" class.


def two_next_to(board, token):
    '''
    Returns the number of pairs of tokens that a
    player has for a given board.
    '''
    pairs = []

    # Horizontal checker
    for j in range(0, 6):
        for i in range(1, 7):

            pair = ((j, i), (j, i-1))

            if (board[j][i] == board[j][i - 1] == token):
                pairs.append(pair)

    # Vertical checker
    for i in range(0, 7):
        for j in range(1, 6):

            pair = ((j, i), (j-1, i))

            if (board[j][i] == board[j - 1][i] == token):
                pairs.append(pair)

    # Diagonal checker
    for i in range(0, 6):
        for j in range(0, 5):

            pair = ((j, i), (j+1, i+1))
    
            if (board[j][i] == board[j + 1][i + 1] == token):
                pairs.append(pair)

            pair = ((j+1, i), (j, i+1))

            if (board[j + 1][i] == board[j][i + 1] == token):
                pairs.append(pair)

    return len(pairs)

                
def three_next_to(board, token):
    '''
    Returns the number of triads of tokens that a
    player has for a given board.
    '''
    triads = []

    # Horizontal checker
    for j in range(0, 6):
        for i in range(2, 7):

            triad = ((j, i), (j, i-1), (j, i-2))

            if (board[j][i] == board[j][i - 1] == board[j][i - 2] == token):
                triads.append(triad)

    # Vertical checker
    for i in range(0, 7):
        for j in range(2, 6):

            triad = ((j, i), (j-1, i), (j-2, i))

            if (board[j][i] == board[j - 1][i] == board[j - 2][i] == token):
                triads.append(triad)

    # Diagonal checker
    for i in range(0, 5):
        for j in range(0, 4):

            triad = ((j, i), (j+1, i+1), (j+2, i+2))
    
            if (board[j][i] == board[j + 1][i + 1] == board[j + 2][i + 2] == token):
                triads.append(triad)

            triad = ((j+2, i), (j+1, i+1), (j, i+2))

            if (board[j + 2][i] == board[j + 1][i + 1] == board[j][i + 2] == token):
                triads.append(triad)

    return len(triads)


if __name__ == "__main__":
    game = Connect4()
    game.move(2, "X")
    game.move(2, "X")
    game.move(2, "X")
    game.move(1, "X")
    game.move(3, "X")
    game.move(3, "X")
    game.move(4, "X")
    game.move(4, "O")
    game.move(4, "X")

    game.print_board()
    print(three_next_to(game.board, "X"))