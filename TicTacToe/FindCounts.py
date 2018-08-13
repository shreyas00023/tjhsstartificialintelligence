import random
import time
goalcount = 0
class TicTacToe:
    def __init__(self, state, parent, player):
        if state==None:
            self.state = [[None,None,None],[None,None,None],[None,None,None]]
        else:
            self.state = state
        self.parent = parent
        self.player = player
    def get_children(self):
        row=0
        col=0
        children = []
        turn = 'X'
        if self.player == 'X':
            turn = 'O'
        for r in self.state:
            col=0
            for c in r:
                if c == None:
                    temp = [list(row) for row in self.state]
                    temp[row][col] = turn
                    child = TicTacToe(temp, self, turn)
                    children.append(child)
                col = col+1
            row=row+1
        return children               
    def winner(self, p):
        if self.state[1][1] == p and self.state[0][0]==p and self.state[2][2]==p:
            return True
        if self.state[1][1] == p and self.state[1][0]==p and self.state[1][2]==p:
            return True
        if self.state[0][1] == p and self.state[0][0]==p and self.state[0][2]==p:
            return True
        if self.state[2][1] == p and self.state[2][0]==p and self.state[2][2]==p:
            return True
        if self.state[0][1] == p and self.state[1][1]==p and self.state[2][1]==p:
            return True
        if self.state[1][0] == p and self.state[0][0]==p and self.state[2][0]==p:
            return True
        if self.state[1][2] == p and self.state[0][2]==p and self.state[2][2]==p:
            return True
        if self.state[0][2] == p and self.state[1][1]==p and self.state[2][0]==p:
            return True
        check = False
        for r in self.state:
            for c in r:
                if c == None:
                    check = True
                    break
        if check==True:
            return True
    def __str__(self):
        s=''
        for r in self.state:
            for c in r:
                s+= str(c)+"\t"
            s+='\n'
        return s
def tree_search(n, firstTime):
   global goalcount
   goalcount = 0
   fringe = [n]
   while (True):
      if not fringe:
          print(time.time()-firstTime)
          print("Number of Games", goalcount)
          return False
      turn = 'X'
      if n.player == 'X':
          turn = 'O'
      if n.winner(turn):
         goalcount = goalcount+1    
      child = n.get_children()
      fringe.extend(child)
      n = fringe.pop()
node = TicTacToe(state=None, parent=None, player='X')
tree_search(node, time.time())
    
