from core import *
memorymax = {}
memorymin = {}
def minimax_strategy(size):
    def strategy(board, player):
        return minimax(board, player, size)
    return strategy
def minimax(board, player, max_d):
    if player == "X": return max_dfs(board, player, max_d, 0)[1]
    if player == "O": return min_dfs(board, player, max_d, 0)[1]
def max_dfs(board, player, max_d, current_d):
    if terminal_test(board):
        return terminal_value(board), None
##    if current_d = max_d:
##        return winner(board), None
    v = -100000
    move = -1
    for m in actions(board):
        new_board = make_move(board, player, m)
        if (new_board, player) in memorymax:
            new_value = memorymax[(new_board, player)]
        else:
            new_value = min_dfs(make_move(board, player, m), toggle(player), 0, current_d+1)[0]
            memorymax[(new_board, player)] = new_value
        if new_value == 1:
            v = 1
            move = m
            return v, move
        if new_value>v:
            v = new_value
            move = m
    return v, move
def min_dfs(board, player, min_d, current_d):
    if terminal_test(board):
        return terminal_value(board), None
##    if current_d = min_d:
##        return winner(board), None
    v = 1000000
    move = -1
    for m in actions(board):
        new_board = make_move(board, player, m)
        if (new_board, player) in memorymin:
            new_value = memorymin[(new_board, player)]
        else:
            new_value = max_dfs(make_move(board, player, m), toggle(player), 0, current_d+1)[0]
            memorymin[(new_board, player)] = new_value
        if new_value == -1:
            v=-1
            move = m
            return v, move
        if new_value<v:
            v = new_value
            move = m
    return v, move
def terminal_value(board):
    if winner(board) == "X":
        return 1
    if winner(board) == "O":
        return -1
    else:
        return 0
def human(board, player):
    move = input("Type Move: ")
    return int(move)
def random(board, player):
    return actions(board).pop()
    
