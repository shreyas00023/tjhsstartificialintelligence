import numpy as np
import random
import itertools

a = np.array([0,0,1])
b = np.array([0,1,1])
c = np.array([1,0,1])
d = np.array([1,1,1])

t_set = [(a,0), (b,0), (c,0), (d,1)]

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
        print(f)
        w = perceptron_learn(f, size)
        print(w)
        curr_count=0
        for t in f:
            g = const(np.dot(w, t[0]))
            if g == t[1]:
                curr_count += 1
        if curr_count==len(f): correct_count+=1
    return correct_count

def majority_test():
    input = generate_nonarray_input(10)
    full_array = []
    for i in input:
        one = i.count(1)
        zero = i.count(0)
        if one>zero: full_array.append((np.array(i),1))
        else: full_array.append((np.array(i),0))
    for s in range(5, 100, 5):
        random.shuffle(full_array)
        training_set = full_array[:s]
        #print(len(training_set))
        #training_set = random.sample(full_array,s)
        test_set = full_array[s:len(full_array)]
        #print(len(test_set))
        w = perceptron_learn(training_set,10)
        #print(w)
        curr_count = 0
        for t in test_set:
            g = const(np.dot(w, t[0]))
            if g == t[1]:
                curr_count += 1
        print(str(s) + "\t" + str(curr_count/len(test_set)))

#print(test(4))
#majority_test()
