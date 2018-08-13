import numpy as np
import math
class NN:
    def __init__(self,arr):
        self.inputs = [1]*(arr[0]+1)
        self.weights = []
        for i in range(len(arr)-1):
            self.weights.append(np.tile(1,(arr[i]+1,arr[i+1])))
        print(self.weights)
    def eval(self):
        tempin = self.inputs
        for a in self.weights:
            val = np.dot(tempin,a)
            tempin = []
            for b in val:
                tempin.append(self.sigmoid(b))
            tempin.append(1)
        return tempin[:len(tempin)-1]
    def sigmoid(self,dot):
        #return dot
        return 1/(1+math.exp(-dot))
net = NN([8,6,4,2,4,6,8,1])
#print(net.eval())