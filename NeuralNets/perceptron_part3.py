from multiperceptron import Percept
from multiperceptron import Input
import random
import math
import numpy as np

x1 = Input()
x2 = Input()

one = Percept(None,None)
two = Percept(None,None)
three = Percept(None,None)

one.set_inputs([x1,x2])
two.set_inputs([x1,x2])
three.set_inputs([one,two])

def func(weights, output):
    one.set_weight_threshold([weights[0],weights[1]],weights[2])
    two.set_weight_threshold([weights[3], weights[4]], weights[5])
    three.set_weight_threshold([weights[6], weights[7]], weights[8])
    arr = []
    for a in range(2):
        for b in range(2):
            x1.set_value(a)
            x2.set_value(b)
            arr.append(three.eval())
    return arr

def error(weights, output):
    one.set_weight_threshold([weights[0],weights[1]],weights[2])
    two.set_weight_threshold([weights[3], weights[4]], weights[5])
    three.set_weight_threshold([weights[6], weights[7]], weights[8])
    totalerr = 0
    cnt = 0
    for a in range(2):
        for b in range(2):
            x1.set_value(a)
            x2.set_value(b)
            totalerr+= abs(three.eval()-output[cnt])
            cnt+=1
    return totalerr
#print(error([[0,0,0],[0,0,0],[0,0,0]],[0,1,1,0]))
def hill_climber(lamb):
    count = 0
    output = [0,1,1,0]
    w = [random.uniform(-1,1) for k in range(9)]
    target = 0.1
    restart = 0
    direc = [random.uniform(-1,1) for m in range(9)]
    while error(w,output)>target:
        count+=1
        restart+=1
        #print(error(w,output))
        delta = [random.random()*lamb*direc[j] for j in range(9)]
        temp = [w[l]+delta[l] for l in range(9)]
        if error(temp,output)<error(w,output):
            w = temp
        else:
            direc = [random.uniform(-1, 1) for m in range(9)]
        if (restart > 500):
            restart=0
            w = [random.uniform(-1,1) for k in range(9)]
    return count
curr = 0.1
num = 20
print(hill_climber(0.7))
for i in np.arange(0.1,2.1,.1):
    s = 0
    for g in range(num):
        s+=hill_climber(i)
    print(str(i)+"\t"+str(s/num))