import Othello_Core as core
import random, time

class Strategy(core.OthelloCore):
    SQUARE_WEIGHTS = [
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 120, -20, 20, 5, 5, 20, -20, 120, 0,
        0, -20, -40, -5, -5, -5, -5, -40, -20, 0,
        0, 20, -5, 15, 3, 3, 15, -5, 20, 0,
        0, 5, -5, 3, 3, 3, 3, -5, 5, 0,
        0, 5, -5, 3, 3, 3, 3, -5, 5, 0,
        0, 20, -5, 15, 3, 3, 15, -5, 20, 0,
        0, -20, -40, -5, -5, -5, -5, -40, -20, 0,
        0, 120, -20, 20, 5, 5, 20, -20, 120, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    ]
    def __init__(self):
        pass
    def is_valid(self, move):
        return move in self.squares()
    def opponent(self, player):
        if player == core.WHITE:
            return core.BLACK
        return core.WHITE
    def find_bracket(self, square, player, board, direction):
        bracket = square+direction
        if board[bracket] == player:
            return None
        opp = self.opponent(player)
        while board[bracket] == opp:
            bracket = bracket+direction
        if board[bracket] == core.OUTER or board[bracket] == core.EMPTY:
            return None
        else:
            return bracket
    def is_legal(self, move, player, board):
        check = False
        for d in core.DIRECTIONS:
            if self.find_bracket(move, player, board, d):
                check = True
        return board[move] == core.EMPTY and check
    def make_move(self, move, player, board):
        board[move] = player
        for n in core.DIRECTIONS:
            self.make_flips(move, player, board, n)
        return board
    def make_flips(self, move, player, board, direction):
        bracket = self.find_bracket(move, player, board, direction)
        if not bracket:
            return
        square = move+direction
        while square != bracket:
            board[square] = player
            square = square+direction
    def legal_moves(self, player, board):
        moves = [n for n in self.squares() if self.is_legal(n, player, board)]
        return moves
    def any_legal_move(self, player, board):
        return len(self.legal_moves(player, board)) > 0
    def next_player(self,board,prev_player):
        other = self.opponent(prev_player)
        if self.any_legal_move(other, board):
            return other
        elif self.any_legal_move(prev_player, board):
            return prev_player
        return None
    def score(self, player, board):
        user = 0
        other = 0
        opp = self.opponent(player)
        for sq in self.squares():
            piece = board[sq]
            if piece == player:
                user = user+1
            elif piece == opp:
                other = other+1
        return user-other
    def random_strategy(self, player, board, maxdepth):
        possible = self.legal_moves(player, board)
        return random.choice(possible)
    def alphabetasearch(self, player, board, max_depth):
        if player == core.BLACK:
            return self.max_dfs(board, player, -10000000, 100000000, max_depth, 0)[1]
        else:
            return self.min_dfs(board, player, -10000000, 100000000, max_depth, 0)[1]
    def max_dfs(self, board, player, alpha, beta, max_d, current_d):
        if current_d == max_d:
            return self.weighted_score(board), None
##        if not self.any_legal_move(player, board):
##            if self.any_legal_move(self.opponent(player), board):
##                return self.weighted_score(player, board)-100, None
##            elif weighted_score(core.BLACK, board) > 0:
##                return 100000000, None
##            elif weighted_score(core.BLACK, board) < 0:
##                return -10000000, None
##            else:
##                return 0, None
        elif not self.next_player(board,player):
            return self.score(player, board), None
        v = -10000000
        move = -1
        for m in self.legal_moves(player, board):
            new_v = self.min_dfs(board, player,alpha, beta, max_d, current_d+1)[0]
            if new_v>v:
                v = new_v
                move = m
            if v>=beta: return v, move
            alpha = max(alpha, v)
        return v, move
    def min_dfs(self, board, player,alpha, beta, max_d, current_d):
        if current_d == max_d:
            return self.weighted_score(board), None
##        if not self.any_legal_move(player, board):
##            if self.any_legal_move(self.opponent(player), board):
##                return self.weighted_score(player, board)+100, None
##            elif weighted_score(core.BLACK, board) > 0:
##                return 100000000, None
##            elif weighted_score(core.BLACK, board) < 0:
##                return -10000000, None
##            else:
##                return 0, None
        elif not self.next_player(board, player):
            return self.score(player,board), None
        v = 10000000
        move = -1
        for m in self.legal_moves(player, board):
            new_v = self.max_dfs(board, player, alpha, beta, max_d, current_d+1)[0]
            if new_v<v:
                v = new_v
                move = m
            if v<=alpha: return v, move
            beta = min(beta, v)
        return v, move
    def minimax(self, player, board, maxdepth):
        if player == core.BLACK: return self.max_dfs_single(board, player, maxdepth, 0)[1]
        if player == core.WHITE: return self.min_dfs_single(board, player, maxdepth, 0)[1]
    def max_dfs_single(self, board, player, max_d, current_d):
        if current_d == max_d:
            return self.weighted_score(board), None
##        if not self.any_legal_move(player, board):
##            if self.any_legal_move(self.opponent(player), board):
##                return self.weighted_score(player, board)-1000, None
####            return self.score(player, board)
##            elif self.weighted_score(core.BLACK, board) > 0:
##                return 100000000, None
##            elif self.weighted_score(core.BLACK, board) < 0:
##                return -10000000, None
##            else:
##                return 0, None
        if self.next_player(board, player) == None:
            return self.score(player,board), None
        v = -10000000
        move = -1
        for m in self.legal_moves(player, board):
            new_v = self.min_dfs_single(board, player, max_d, current_d+1)[0]
            if new_v>v:
                v = new_v
                move = m
        return v, move
    def min_dfs_single(self, board, player, max_d, current_d):
        if current_d == max_d:
            return self.weighted_score(board), None
##        if not self.any_legal_move(player, board):
##            if self.any_legal_move(self.opponent(player), board):
##                return self.weighted_score(player, board)+1000, None
##            elif self.weighted_score(core.BLACK, board) > 0:
##                return 100000000, None
##            elif self.weighted_score(core.BLACK, board) < 0:
##                return -10000000, None
##            else:
##                return 0, None
        if self.next_player(board,player) == None:
            return self.score(player, board), None

        v = 10000000
        move = -1
        for m in self.legal_moves(player, board):
            new_v = self.max_dfs_single(board, player, max_d, current_d+1)[0]
            if new_v<v:
                v = new_v
                move = m
        return v, move
    def weighted_score(self, board):
        total = 0
        for sq in self.squares():
            if board[sq] == core.BLACK:
                total = total+self.SQUARE_WEIGHTS[sq]
            elif board[sq] == core.WHITE:
                total = total-self.SQUARE_WEIGHTS[sq]
        return total
    def best_strategy(self, board, player, best_move, still_running):
         """
    :param board: a length 100 list representing the board state
    :param player: WHITE or BLACK
    :param best_move: shared multiptocessing.Value containing an int of
            the current best move
    :param still_running: shared multiprocessing.Value containing an int
            that is 0 iff the parent process intends to kill this process
    :return: best move as an int in [11,88] or possibly 0 for 'unknown'
    """
         depth = 1
         while still_running.value>0:
             time.sleep(1)
             best_move.value = self.alphabetasearch(player, board, depth)
             depth = depth+1
             


            
    
    
