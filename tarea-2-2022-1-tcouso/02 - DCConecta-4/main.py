import time

from score import two_next_to, three_next_to
from player import HumanPlayer, AiPlayer, random_move
from game import Connect4


def main(verbose=True, sleep_time=0.5):
    # If you don't want prints, change verbose to False

    # The human player is always 'X' and the computer is 'O'
    player1 = AiPlayer(token = "X", score_function = two_next_to)
    player2 = AiPlayer(token = "O", score_function = three_next_to)

    # If you want to play against the computer then write the following code: 
    # player1 = HumanPlayer(token = "X")

    # Game metrics

    # Desicion times
    player1_desicion_times = []
    player2_decision_times = []

    # Number of moves
    num_of_moves = 0

    # Bombs used by each player
    player1_bomb_moves = {
        "classic": 0,
        "vertical": 0,
        "horizontal": 0
    }
    player2_bomb_moves = {
        "classic": 0,
        "vertical": 0,
        "horizontal": 0
    }


    # First, we initialize the game 
    match = Connect4()
    # Print board
    if verbose:
        match.print_board()
        print('To play: enter an integer between 1 to 7 ' +
            'corresponding to each column in the board. ' +
            'Whoever stacks 4 pieces next to each other, ' +
            'either horizontally, vertically or diagonally wins.')

    # Turns and game. "game" represents if the game is over or not
    game = False

    # First move made is random, for variability of game purpuses
    p1_first_move = True
    p2_first_move =  True

    while not game:
        # X player (human player)

        if p1_first_move:
        # First player 1 move is random
            pos, bomb = random_move()
            p1_first_move = False
        else:
        # The player chooses his move
            t0 = time.process_time()
            pos, bomb = player1.pick_movement(match)
            t1 = time.process_time()

            # Save player 1 decision time
            player1_desicion_times.append(t1 - t0)

            


        # Tie case
        if pos is None:
            winner = "TIE"
            if verbose:
                print("Tie")
            break

        if verbose:
            print(f"Player 1 Turn {player1.token}")
            print(f"Player 1 played in column {pos} with the use of {bomb[1]} bomb")


        # Use the bomb if one of them is chosen
        if bomb[0]:

            if bomb[1] == "vertical":
                match.vertical_bomb(pos)
                player1.vertical_bomb_available = False

                # Register bomb use
                player1_bomb_moves["vertical"] += 1

            elif bomb[1] == "horizontal":
                match.horizontal_bomb(pos)
                player1.horizontal_bomb_available = False

                # Register bomb use
                player1_bomb_moves["horizontal"] += 1

            elif bomb[1] == "classic":
                match.classic_bomb(pos)
                player1.classic_bomb_available = False

                # Register bomb use
                player1_bomb_moves["classic"] += 1

        # Move
        else:
            match.move(pos, player1.token)

        if verbose:          
            match.print_board()
        # Check if the game is over 
        game = match.check_win(player1.token)       
        if game:
            if verbose:
                print('X wins!')
            winner = 'X'
            break

        # Sleep time activated if verbose
        if verbose:
            time.sleep(sleep_time)

        # First player 2 move is random
        if p2_first_move:
            pos, bomb = random_move()
            p2_first_move = False
        else:
        # The computer chooses his move
            t0 = time.process_time()
            pos, bomb = player2.pick_movement(match)
            t1 = time.process_time()

            # Save player 2 decision times
            player2_decision_times.append(t1 - t0)

        # Tie case
        if pos is None:
            winner = "TIE"
            if verbose:
                print("Tie")
            break


        if verbose:
            print(f"Player 2 Turn {player2.token}")
            print(f"Player 2 played in column {pos} with the use of {bomb[1]} bomb")


        # Use the bombs
        if bomb[0]:


            if bomb[1] == "vertical":
                match.vertical_bomb(pos)
                player2.vertical_bomb_available = False

                # Register bomb use
                player2_bomb_moves["vertical"] += 1

            elif bomb[1] == "horizontal":
                match.horizontal_bomb(pos)
                player2.horizontal_bomb_available = False

                # Register bomb use
                player2_bomb_moves["horizontal"] += 1

            elif bomb[1] == "classic":
                match.classic_bomb(pos)
                player2.classic_bomb_available = False

                # Register bomb use
                player2_bomb_moves["classic"] += 1

        # Move
        else:
            match.move(pos, player2.token)
        if verbose:
            match.print_board()

        # Increase number of moves
        num_of_moves += 1

        # Check if the game is over
        game = match.check_win(player2.token)       
        if game:
            if verbose:
                print('O wins!')
            winner = 'O'

        

    if verbose:
        print('Good game.')

    # Game metrics

    p1_mean_decision_time = sum(player1_desicion_times) / len(player1_desicion_times)
    p2_mean_decision_time = sum(player2_decision_times) / len(player2_decision_times)


    return_list = [
        winner, 
        num_of_moves, 
        p1_mean_decision_time, 
        player1_bomb_moves["classic"],
        player1_bomb_moves["vertical"],
        player1_bomb_moves["horizontal"],
        p2_mean_decision_time,
        player2_bomb_moves["classic"],
        player2_bomb_moves["vertical"],
        player2_bomb_moves["horizontal"],
        ]

    return return_list

if __name__ == '__main__':
    main()
