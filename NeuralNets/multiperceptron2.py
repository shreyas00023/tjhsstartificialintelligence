from multiperceptron import Percept
from multiperceptron import Input
import random

x1 = Input()
x2 = Input()
# AND = Percept([1, 1], 1.5)
# OR = Percept([1, 1], .5)
# NAND = Percept([-1, -1], -1.5)
# NAND2 = Percept([-1, -1], -1.5)
# NAND.set_inputs([x1, x2])
# OR.set_inputs([x1, x2])
# AND.set_inputs([NAND, OR])
# xor = AND
# OR.set_inputs([x1,x2])
# NAND.set_inputs([x1,x2])
# NAND2.set_inputs([OR, NAND])
# xnor = NAND2
node1 = Percept([1,0],-1)
node2 = Percept([-1,0],-1)
node3 = Percept([0,1],-1)
node4 = Percept([0,-1],-1)
node1.set_inputs([x1, x2])
node2.set_inputs([x1, x2])
node3.set_inputs([x1, x2])
node4.set_inputs([x1,x2])
c = 1.5
AND1 = Percept([1, 1], c)
AND2 = Percept([1, 1], c)
AND3 = Percept([1, 1], c)
AND1.set_inputs([node1,node2])
AND2.set_inputs([node3,node4])
AND3.set_inputs([AND1,AND2])
#AND3.set_inputs([node1,node2,node3,node4])

correct = 0
total = 0
while total<10000:
    a = random.uniform(-1.5,1.5)
    b = random.uniform(-1.5, 1.5)
    x1.set_value(a)
    x2.set_value(b)
    run = AND3.eval()
    if a**2+b**2<=1 and run>=.5:
        correct+=1
    if a**2+b**2>1 and run<.5:
        correct+=1
    total+=1
print((correct/total)*100)
# for a in range(2):
#     for b in range(2):
#         x1.set_value(a)
#         x2.set_value(b)
#         print(a, b, AND3.eval())