import random
class TicTacToe:
    def __init__(self):
        self.state = [[None,None,None],[None,None,None],[None,None,None]]
    def post_move(self, row, col):
        self.state[row][col] = 'X'
    def get_move(self):
        if self.notover():
            randrow = random.randint(0,2)
            randcol = random.randint(0,2)
            while self.state[randrow][randcol] != None:
                randrow = random.randint(0,2)
                randcol = random.randint(0,2)
            self.state[randrow][randcol] = 'O'
            return randrow, randcol
    def notover(self):
        check = False
        for r in self.state:
            for c in r:
                if c == None:
                    check = True
        return check
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
    def __str__(self):
        s=''
        for r in self.state:
            for c in r:
                s+= str(c)+"\t"
            s+='\n'
        return s
    
