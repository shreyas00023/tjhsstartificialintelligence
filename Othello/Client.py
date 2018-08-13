import pickle
import strategy as ai
import Strategy2 as ai2
from Othello_Core import *
import time

#############################################################
# client.py
# a simple tic-tac-toe client
# plays 2 strategies against each other and keeps score
# imports strategies from "strategies.py" as ai
# rest of functionality is stored in core.py
#
# Patrick White: December 2016
############################################################
temp = ai.Strategy()
other = ai2.Strategy2()
BLACK_STRATEGY = temp.alpha_beta_strategy(3)
WHITE_STRATEGY = other.alpha_beta_strategy(3)
ROUNDS = 10
MAXD = 3
# see core.py for constants: MAX, MIN, TIE

def play(strategy_BLACK, strategy_WHITE):
    board = temp.initial_board()
    player = BLACK
    current_strategy ={BLACK: strategy_BLACK, WHITE: strategy_WHITE}
    while player is not None:
        move = current_strategy[player](player, board)
        board = temp.make_move(move, player, board)
        #print(temp.print_board(board))
        player = temp.next_player(board, player)
    return board, temp.score(BLACK, board) # returns "X" "O" or "TIE"


def main(startTime):
    j = []
    totalwins = 0
    for i in range(ROUNDS):
        try:
            game_result = play(BLACK_STRATEGY, WHITE_STRATEGY)
            j.append(game_result)
            #print("Winner: ", game_result)
        except temp.IllegalMoveError as e:
            print(e)
            j.append("FORFEIT")
        if game_result[1] > 0:
            totalwins = totalwins+1
##    print(temp.print_board(game_result[0]))
##    print("Score: ", game_result[1])
##    winner = "WHITE"
##    if game_result[1] > 0:
##        winner = "BLACK"
##    print("Winner: ", winner)
    print("Black: ",totalwins)
    print("White: ", 10-totalwins)
    print(time.time()-startTime, "ms")


if __name__ == "__main__":
    main(time.time())

    
