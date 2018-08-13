#Shreyas Angara Period 7 4/21/17
import numpy as np
import math
import random
class Percept:
    def __init__(self, weights, threshold):
        self.w = np.array(weights)
        self.threshold = threshold
    def step(self, dot):
        k=4.65
        # if dot > self.threshold: return 1
        # return 0
        try:
            ans = 1/(1+math.exp(-k*(dot-self.threshold)))
        except OverflowError:
            ans = 0
        return ans
    def eval(self):
        inputValues = []
        for i in self.inputs:
            inputValues.append(i.eval())
        return self.step(np.dot(self.w, inputValues))
    def set_inputs(self, l):
        self.inputs = np.array(l)
    def set_weight_threshold(self, weights, threshold):
        self.w = np.array(weights)
        self.threshold = threshold
class Input(Percept):
    def __init__(self):
        pass
    def set_value(self, i):
        self.value = i
    def eval(self):
        return self.value
def perceptron_learn(training_set,size):
    arr = [0]*(size)
    arr.append(1)
    w = np.array(arr)
    constant = 1
    for b in range(1000):
        for t in training_set:
            f = const(np.dot(w, t[0]))
            w = w + constant*(t[1]-f)*t[0]
    return w
def const(dot):
    if dot>0: return 1
    return 0

def generate_input(size):
    l = [[int(b) for b in list(bin(i)[2:].zfill(size))] for i in range(2**size)]
    for s in l: s.append(1)
    return np.array(l)

def generate_nonarray_input(size):
    l = [[int(b) for b in list(bin(i)[2:].zfill(size))] for i in range(2**size)]
    for s in l: s.append(1)
    return l

def generate_output(size):
    l = [[int(b) for b in list(bin(i)[2:].zfill(2**size))] for i in range(2 ** (2**size))]
    return l

def test(size):
    weights = []
    input = generate_input(size)
    output = generate_output(size)
    correct_count = 0
    func_array = []
    for x in range(len(output)):
        t_array = []
        for y in range(len(input)):
            t_array.append((input[y],output[x][y]))
        func_array.append(t_array)
    for f in func_array:
        w = perceptron_learn(f, size)
        curr_count=0
        for t in f:
            g = const(np.dot(w, t[0]))
            if g == t[1]:
                curr_count += 1
        if curr_count==len(f):
            correct_count+=1
            weights.append(w.tolist())
    return weights
functions = test(2)
perceptrons = []
#print(test(2))
for w in test(2):
    perceptrons.append(Percept([w[0],w[1]], -w[2]))
correct_count=0
x1 = Input()
x2 = Input()
for a in perceptrons:
    node1=Percept(a.w, a.threshold)
    for b in perceptrons:
        node2=Percept(b.w, b.threshold)
        for c in perceptrons:
            node3=Percept(c.w, c.threshold)
            node3.set_inputs([x1,x2])
            node2.set_inputs([x1,x2])
            node1.set_inputs([node2,node3])
            output = []
            for i in range(2):
                for j in range(2):
                    x1.set_value(i)
                    x2.set_value(j)
                    output.append(node1.eval())
            #print(output)
            if output == [0,1,1,0]:
                print(functions.index([node1.w.tolist()[0],node1.w.tolist()[1],-node1.threshold]),functions.index([node2.w.tolist()[0],node2.w.tolist()[1],-node2.threshold]),functions.index([node3.w.tolist()[0],node3.w.tolist()[1],-node3.threshold]))
                correct_count+=1
print(correct_count)
# x1 = Input()
# x2 = Input()
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
# for a in range(2):
#     for b in range(2):
#         x1.set_value(a)
#         x2.set_value(b)
#         print(a, b, xnor.eval())