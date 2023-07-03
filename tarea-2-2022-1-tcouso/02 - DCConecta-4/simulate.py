import pandas as pd
from main import main

def simulate(n: int):
    """
    Simulates an amount of n games. Returns a list in wich each row
    is a game with a winner, mean decision times and number of moves 
    for each player.
    """
    winners = []
    print(f"Starting simulation of {n} games...")
    for _ in range(n):
        winner = main(verbose=False)
        winners.append(winner)
    print("Simulation completed")

    return winners

if __name__ == "__main__":
    N = 100
    winners = simulate(N)

    df = pd.DataFrame(
        winners, 
        columns=[
            "winner", 
            "num-of-moves",
            "x-mean-decision-time", 
            "x-classic-bombs",
            "x-vertical-bombs",
            "x-horizontal-bombs",
            "o-mean-decision-time",
            "o-classic-bombs",
            "o-vertical-bombs",
            "o-horizontal-bombs"
            ]
    )
    df.to_csv(f"{N}-simulations.csv")