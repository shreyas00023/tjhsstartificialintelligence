import math
import heapq
import time
def dist(lat1, lon1, lat2, lon2):
     temp1 = float(lat1)
     temp2 = float(lon1)
     temp3 = float(lat2)
     temp4 = float(lon2)
     R = 6371000
     pho1 = math.radians(temp1)
     pho2 = math.radians(temp3)
     phochange = math.radians(temp3-temp1)
     vlength = math.radians(temp4-temp2)
     a = math.sin(phochange/2) * math.sin(phochange/2) + math.cos(pho1) * math.cos(pho2) * math.sin(vlength/2) * math.sin(vlength/2)
     c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
     d = R * c
     d= d*0.000621371
     return d
cities = {}
names = open("rrNodeCity.txt", 'r')
for line in names:
     first = line[0:7]
     name = line[8:len(line)]
     name = name.strip()
     cities[name] = first
position = {}
file = open("rrNodes.txt", 'r')
for line in file:
    temp = line.split()
    position[temp[0]] = (temp[1], temp[2])
edges = open("rrEdges.txt", 'r')
edge = {}
for line in edges:
      string = line.split()
      start = string[0]
      end = string[1]
      d = dist(position[start][0],position[start][1], position[end][0], position[end][1])
      if start not in edge:
           edge[start] = {end:d}
      else:
           edge[start][end] = d
      if end not in edge:
           edge[end] = {start: d}
      else:
           edge[end][start] = d
class Node:
     def __init__(self, state, goal):
          self.state = state
          self.acost = 0
          self.ecost = 0
          self.goal = goal
     def __lt__(self, other):
          return self.acost+self.ecost<=other.acost+other.ecost
     def getChildren(self):
          children = []
          for n in edge[self.state].keys():
               children.append(n)
          return children
     def expand(self):
          successors = []
          for c in self.getChildren():
               child = Node(c, self.goal)
               child.acost = self.acost+edge[self.state][c]
               child.ecost = dist(position[self.state][0], position[self.state][1], position[self.goal][0], position[self.goal][0])
               successors.append(child)
          return successors
def graph_search(start, goal, startTime):
     node = Node(cities[start], cities[goal])
     closed = set()
     fringe = [node]
     while(True):
          if not fringe:
               return None
          n = heapq.heappop(fringe)
          if n.state == cities[goal]:
               print("%20s %20s %8.3f %4.3f" % (start, goal, n.acost, time.time()-startTime), file=outfile)
               return True
          if n.state not in closed:
               closed.add(n.state)
               arr = n.expand()
               for i in arr:
                    if i not in closed:
                         heapq.heappush(fringe, i)
def railroad(one, two):
    graph_search(one, two, time.time())
inputwords = open("test.txt", 'r')
infile = []
for line in inputwords:
    temp = line.split(',')
    infile.append(temp)
outfile = open("solutions.txt", 'w')
for n in infile:
    railroad(n[0].strip(),n[1].strip())
outfile.close()


          
     
               
          

          
     
    

        
