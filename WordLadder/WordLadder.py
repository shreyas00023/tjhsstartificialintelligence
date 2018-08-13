import time
import heapq
class Word:
    def __init__(self, parent, string, goal, depth):
        self.parent = parent
        self.string = string
        self.goal = goal
        self.depth = depth
    def goalTest(self):
        return self.string == self.goal
    def giveSolution(self):
      #loop through all parents,put them in a list, and print states in reverse
      step = []
      step.append(self.string)
      temp = self
      while temp.parent != None:
         temp = temp.parent
         step.append(temp.string)
      step.reverse()
      words.extend(removedwords)
      return len(step)-1
      #print(step)
    def getChildren(self):
        children = []
        for n in words:
            if self.checkWords(self.string, n):
                temp = Word(self, n, self.goal, self.depth+1)
                children.append(temp)
                removedwords.append(n)
                words.remove(n)
        return children
    def checkWords(self, word1, word2):
        cnt = 0
        for sai in range(0,6):
            if word1[sai] == word2[sai]:
                    cnt = cnt + 1
        if cnt == 5:
            return True
        else:
            return False
    def __lt__(self, other):
        sameself = 0
        sameother = 0
        for i in range(0,6):
            if(self.string[i] != self.goal[i]):
                sameself = sameself+1
            if(other.string[i] != self.goal[i]):
                sameother = sameother+1
        if(sameself+self.depth <= sameother+other.depth):
            return True
        return False
def tree_search(n, firstTime, first):
   removedwords = []
   fringe = [n]
   while (True):
      if not fringe:
          outfile.write(first)
          outfile.write(" "+n.goal)
          outfile.write(" --")
          outfile.write(" %.3f\n" % (time.time()-firstTime) )
          return False
      if n.goalTest():
         outfile.write(first)
         outfile.write(" "+n.goal)
         outfile.write(" "+str(n.giveSolution()))
         outfile.write(" %.3f\n" % (time.time()-firstTime))
         return False    
      child = n.getChildren()
      for c in child:
          heapq.heappush(fringe, c)
      n = heapq.heappop(fringe)
def wordLadder(start, end):
    test = Word(None, start, end, 0)
    tree_search(test, time.time(), start)
file = open("morewords.txt", 'r')
words = []
for line in file:
    words.append(line[:6])
removedwords = []
inputwords = open("puzzlesA.txt", 'r')
infile = []
for line in inputwords:
    temp = line.split()
    infile.append(temp)
outfile = open("solutions.txt", 'w')
for n in infile:
    wordLadder(n[0],n[1])

outfile.close()



                
                
        

            
        
        

        
        
        
