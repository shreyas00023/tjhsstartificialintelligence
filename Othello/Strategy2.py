import random
import Othello_Core as core
import os, signal
import time
from multiprocessing import Process, Value
time_limit = 5
class Strategy2(core.OthelloCore):
    def _init_(self):
        pass
    def is_valid(self, move):
        return isinstance(move, int) and move in self.squares()
    def opponent(self, player):
        return core.BLACK if player is core.WHITE else core.WHITE
    def find_bracket(self, square, player, board, direction):
##        print(board, "this is bracket")
        bracket = square+direction
        if board[bracket] == player:
            return None
        opp = self.opponent(player)
        while bracket<101 and board[bracket] == opp:
            bracket = bracket+direction
        if bracket>100:
            return None
        if board[bracket] == core.OUTER or board[bracket] == core.EMPTY:
            return None
        else:
            return bracket
##        return None if board[bracket] in (core.OUTER, core.EMPTY) else bracket
    def is_legal(self, move, player, board):
##        print(board, "this is is_legal")
        for x in core.DIRECTIONS:
            if self.is_valid(move) and board[move]== core.EMPTY and self.find_bracket(move, player, board, x)!= None:
                return True
        return False
    def make_move(self, move, player, board):
        nboard= list(board)
        if self.is_legal(move, player, board):
            
            nboard[move]= player
            for x in core.DIRECTIONS:
                yourmove= self.find_bracket(move, player, nboard, x)
                if yourmove != None:
                    self.make_flips(move, player, nboard, x)
                        
                
           
        return nboard
    def make_flips(self, move, player, board, direction):
        yourmove= self.find_bracket(move, player, board, direction)
        bracket= move +direction
        while(board[bracket] != board[yourmove]):
            board[bracket]=(player)
            bracket= bracket+direction
        board[bracket]= player
    def legal_moves(self, player, board):
##        print(board, "this is legal_moves")
        lis= []
        for x in range(11, 89):
            a= self.is_legal(x, player, board)
            if(a==True and board[x]==core.EMPTY):
                lis.append(x)
        return lis
    def any_legal_move(self, player, board):
##        print(board, "this is any_legal_move")
        if len(self.legal_moves(player, board))!=0:
            return True
        return False
    def next_player(self, board, prev_player):
##        print(board, "this is next_player")
        if self.any_legal_move(self.opponent(prev_player), board)== True:
            return self.opponent(prev_player)
        elif self.any_legal_move(prev_player, board)==True:
            return prev_player
        else:
            return None
    def score(self, player, board):
        pc=0
        oc=0
        for x in board:
            
            if x== player:
                pc=pc+1
            elif x== self.opponent(player):
                oc=oc+1
        return pc-oc
    def random(self, board, player):
##        if(self.any_legal_move(player, board)):
##        print(board, "this is random")
        r= random.randint(11, 88)
        while r not in self.legal_moves(player, board):
            r= random.randint(11, 88)
        return r
##        return None
    def successors(self,board,player):
        j= []
     
        for move in self.legal_moves(player, board):
            y= self.make_move(move, player, board)
            j.append(y)
            
        return j
    def alpha_beta_strategy(self, max_depth):
        def strategy(player, board):
            return self.alpha_beta_search(board, player, max_depth)
        return strategy            
    def alpha_beta_search(self, board, player, max_depth):
##        print(player, "yes")
        if player== core.BLACK:
            move= self.max_value(board, float("-inf"), float("inf"), player, max_depth)[1]
##            print(move, "aaa")
        elif player== core.WHITE:
            move= self.min_value(board, float("-inf"), float("inf"), player, max_depth)[1]
##            print(move)
        return move
    def evalu(self,board):
        SQUARE_WEIGHTS = [   0, 0, 0, 0, 0, 0, 0, 0, 0, 0,    0, 120, -20, 20, 5, 5, 20, -20, 120, 0,    0, -20, -40, -5, -5, -5, -5, -40, -20, 0,    0, 20, -5, 15, 3, 3, 15, -5, 20, 0,    0, 5, -5, 3, 3, 3, 3, -5, 5, 0,
        0, 5, -5, 3, 3, 3, 3, -5, 5, 0,
        0, 20, -5, 15, 3, 3, 15, -5, 20, 0,
        0, -20, -40, -5, -5, -5, -5, -40, -20, 0,
        0, 120, -20, 20, 5, 5, 20, -20, 120, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0  ]
        a= 0
        for x in self.squares():
            if board[x] == core.WHITE:
                a= a-SQUARE_WEIGHTS[x]
            elif board[x] == core.BLACK:
                a= a+SQUARE_WEIGHTS[x]
        return a
        
    def max_value(self, board, alpha, beta, player, max_depth):
        if self.next_player(board, player)== None:
            return self.score(player, board), None
        if max_depth==0:
##            print("done")
            return self.evalu( board), None
        
        v=float("-inf")
        move=-1
        for s in self.legal_moves(player, board):
            y= self.make_move(s, player, board)
            rrr= self.min_value(y, alpha, beta,self.next_player(board, player), max_depth-1)[0]
            if v < rrr:
                move=s
                v= rrr
##                print(v, move, "bit")
            if v>= beta:
##                print(v,move, "beta")
                return v, move
            alpha= max(alpha, v)
        return v, move
    def min_value(self, board, alpha, beta, player, max_depth):
        if self.next_player(board, player)== None:
            return self.score(player, board), None
        if max_depth==0:
##            print("done")
            return self.evalu(board), None
        v=float("inf")
        move=-1
        for s in self.legal_moves(player, board):
            y= self.make_move(s, player, board)
            rrr=self.max_value(y, alpha, beta, self.next_player(board, player), max_depth-1)[0]
            if v > rrr:
                move=s
                v= rrr
##                print(v, move, "ait")
            if v<= alpha:
##                print(v,move, "alph")
                return v, move
            beta= min(beta, v)
        return v, move


    def best_strategy(self, player, board, best_move, still_running):
        depth=1 #time efficient strategy
        while(still_running.value > 0):
                time.sleep(1) 
                best_move.value = self.alpha_beta_search(player, board, depth)
                depth= depth+1
        
    def get_move(self):
        best_move = Value("i",0)
        running = Value("i",1)
        p = Process(target=best_strategy, args=("", "",  best_move, running)) # create a sub process
        p.start()	# start it
        t1 = time.time()
        print("starting %i" % p.pid)
        p.join(time_limit)		# give the process time to run, and rejoin (works if it's done)
        if p.is_alive():
                print("Not finished within time limit")
                time.sleep(3)		# let it run a little longer
                running.value = 0	# tell it we're about to stop
                time.sleep(0.1)		# wait a bit
                p.terminate()		# terminate
                time.sleep(0.1)		# wait a bit

        if p.is_alive(): 
                print("STILL ALIVE: Force Kill")
                os.kill(p.pid, signal.SIGKILL)	# make the OS destroy it
        t2 = time.time()
        
        move = best_move.value	# get the final best move

        print("Ended  %i" % p.pid)
        print("Elapsed time: %3.5f" % (t2 - t1))
        print("Best move (i.e. number of seconds running*100 = )", best_move.value)
        

                   
            

    
            
        
    
                
