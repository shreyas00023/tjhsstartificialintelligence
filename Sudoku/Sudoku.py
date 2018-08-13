# Name: Shreyas Angara
# Block: 7
# Email: 2018sangara@tjhsst.edu
import time
import math
import heapq
from collections import deque
import random
#Disclaimer: Saiteja Bavera helped me understand and fix my assign method
goalcount = 0
nodecount = 0
class Sudoku:
    def __init__(self, state=None, choices=None):
        """ creates an nQueens board where state is a list of n integers,
            one per column,
            and choices is a list of sets,
            n is the size
            parent is the state predecessor in a search
        """
        global nodecount
        nodecount = nodecount+1
        if state == None:
            self.state = [None]*81
        else:
            self.state = state
        if choices == None:
            self.choices = []
            for a in range(81):
                c = set()
                for b in range(1,10):
                    c.add(b)
                self.choices.append(c)
        else:
            self.choices = choices

    def assign(self, var, value):
        """ updates the state by setting state[var] to value
            also propgates constraints and updates choices
        """
##        self.state[var] = value
##        self.choices[var]=set()
##        row = var//9
##        col = var%9
##        for i in range(81):
##            if i//9 == row or i%9 == col:
##                self.choices[i].difference_update({value})
##        x = row - (row%3)
##        y = col - (col%3)
##        for i in range(x, x+3):
##            for j in range(y, y+3):
##                self.choices[9*i+j].difference_update({value})
##        for i in range(81):
##            if len(self.choices[i])==1:
##                self.assign(i, self.choices[i].pop())
        self.state[var] = value
        self.choices[var] = set()
        row = var//9
        col = var%9
        for i in range(0,81):
            if i//9 == row:
                self.choices[i].difference_update({value})
        for i in range(0,81):
            if i%9== col:
                self.choices[i].difference_update({value})
        distx = row - (row%3) 
        disty = col - (col%3)
        print(distx, disty)
        for i in range(distx, distx+3):
            for j in range(disty, disty+3):
                self.choices[i*9 + j].difference_update({value})

    def goal_test(self):
        """ returns True iff state is the goal state """
        return None not in self.state           

    def get_next_unassigned_var(self):
        """ returns the index of a column that is unassigned and
            has valid choices available """
#DFS
#        return self.state.index(None)
#Random
##        pos = random.randint(0,80)
##        while(self.state[pos] != None):
##            pos = random.randint(0,80)
##        return pos
#Least_Choice
        size = 100000000000
        index = 0
        for s in range(81):
            if len(self.choices[s])!=0 and len(self.choices[s]) < size and self.state[s] == None:
                size = len(self.choices[s])
                index = s
        return index
#Middle
##       mid = int(self.size/2)
##        index = 0
##        mindist = 100000
##        for n in range(self.size):
##            if len(self.choices[n])!=0 and abs(mid-n)<mindist and self.state[n] == None:
##                index = n
##                mindist = abs(mid-n)
##        return index                       
    def get_choices_for_var(self, var):
        """ returns choices[var], the list of available values
                 for variable var, possibly sorted """
        return self.choices[var]

    def __str__(self):
        """ returns a string representation of the object """
        s=''
        for i,n in enumerate(self.state):
            s += str(n)
            if i%9==8: s+='\n'
        return s


###---------------------------------------------------------------
def dfs_search(board, startTime):
    """ sets board as the initial state and returns a
        board containing an nQueens solution
        or None if none exists
    """
    global goalcount
    goalcount = 0
    global nodecount
    nodecount = 0
    fringe = deque()
    fringe.append(board)
    while True:
        if not fringe:
             return None
        current = fringe.pop()
        goalcount = goalcount +1
        if current.goal_test():
             t = time.time()-startTime
             print(current, t, nodecount) 
             #print("%3.0f %8.0f %8.0f %4.3f %8.0f" % (board, goalcount, nodecount, t, nodecount/t), file=outfile)
             return current
        var = current.get_next_unassigned_var()
        for value in (current.get_choices_for_var(var)):
             temp = current.state.copy()
             child = Sudoku(state=temp, choices=[set(row) for row in current.choices])
             child.assign(var, value)
             fringe.append(child)
##outfile = open("solutions.txt", 'w')
##for n in range(4, 100, 3):
##    dfs_search(n, time.time())
##outfile.close()
node = Sudoku()
begin = "6.2.5.........4.3..........43...8....1....2........7..5..27...........81...6....."
for c in range(81):
    if not begin[c] == '.':
        node.assign(c, int(begin[c]))
dfs_search(node, time.time())

