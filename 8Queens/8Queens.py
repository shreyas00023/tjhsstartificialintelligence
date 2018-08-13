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
class nQueens:
    def __init__(self, state=None, choices=None, n=8, parent=None):
        """ creates an nQueens board where state is a list of n integers,
            one per column,
            and choices is a list of sets,
            n is the size
            parent is the state predecessor in a search
        """
        global nodecount
        nodecount = nodecount+1
        if state == None:
            self.state = [None]*n
        else:
            self.state = state
        self.size = n
        if choices == None:
            self.choices = []
            for a in range(n):
                c = set()
                for b in range(n):
                    c.add(b)
                self.choices.append(c)
            self.parent = parent
        else:
            self.choices = choices

    def assign(self, var, value):
        """ updates the state by setting state[var] to value
            also propgates constraints and updates choices
        """
        self.state[var] = value
        for i in range(self.size):
            dist = abs(var-i)
            self.choices[i].difference_update([value])
            self.choices[i].difference_update([value - dist, value + dist])

    def goal_test(self):
        """ returns True iff state is the goal state """
        return None not in self.state           

    def get_next_unassigned_var(self):
        """ returns the index of a column that is unassigned and
            has valid choices available """
#DFS
##        return self.state.index(None)
#Random
##        pos = random.randint(0,self.size-1)
##        while(self.state[pos] != None):
##            pos = random.randint(0,self.size-1)
##        return pos
#Least_Choice
##        size = 100000000000
##        index = 0
##        for s in range(self.size):
##            if len(self.choices[s])!=0 and len(self.choices[s]) < size and self.state[s] == None:
##                size = len(self.choices[s])
##                index = s
##        return index
#Middle
        mid = int(self.size/2)
        index = 0
        mindist = 100000
        for n in range(self.size):
            if len(self.choices[n])!=0 and abs(mid-n)<mindist and self.state[n] == None:
                index = n
                mindist = abs(mid-n)
        return index                       
    def get_choices_for_var(self, var):
        """ returns choices[var], the list of available values
                 for variable var, possibly sorted """
        return self.choices[var]

    def __str__(self):
        """ returns a string representation of the object """
        return str(self.state)


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
    start = nQueens(n=board)
    fringe = deque()
    fringe.append(start)
    while True:
        if not fringe:
             return None
        current = fringe.pop()
        goalcount = goalcount +1
        if current.goal_test():
             t = time.time()-startTime
             print("%3.0f %8.0f %8.0f %4.3f %8.0f" % (board, goalcount, nodecount, t, nodecount/t), file=outfile)
             return current
        var = current.get_next_unassigned_var()
        for value in (current.get_choices_for_var(var)):
             child = nQueens(state=current.state, choices=[set(row) for row in current.choices], n=current.size, parent=current)
             child.assign(var, value)
             fringe.append(child)
outfile = open("solutions.txt", 'w')
for n in range(4, 100, 3):
    dfs_search(n, time.time())
outfile.close()
    
