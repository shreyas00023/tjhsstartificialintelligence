import random
import math
import numpy
import scipy
import matplotlib

def A(dot):
    # return dot
    return 1 / (1 + math.exp(-dot))
    #return dot/10
def Aprime(dot):
    #return 1/10
    return A(dot)*(1-A(dot))
# def forwardprop(input,weights,dimen,lamb):
#
def backprop(trainingset,dimen,lamb):
    weights = []
    for i in range(len(dimen)-1):
        rows = dimen[i]
        cols = dimen[i+1]
        m1 = []
        for j in range(rows):
            m2 = []
            for k in range(cols):
                m2.append(random.uniform(-1,1))
                #m2.append(0)
            m1.append(m2)
        weights.append(m1)
    # weights.append([[2,3],[-2,-4],[1,-1]])
    # weights.append([[1,2],[-2,-1]])
    error = 90
    cnt = 0
    while error>.76:
        overallavals = []
        print(error)
        for nose in trainingset:
            for a in range(1):
                error = 0
                avals = []
                dotvals = []
                deltavals = []
                azero=[]
                dotzero = []
                bvals = []
                for x in range(len(dimen)):
                    blevel = []
                    for y in range(dimen[x]):
                        # blevel.append(random.uniform(-1,1))
                        blevel.append(0)
                    bvals.append(blevel)
                #print(bvals)
                for b in range(dimen[0]):
                    azero.append(nose[0][b])
                    dotzero.append(0)
                avals.append(azero)
                dotvals.append(dotzero)
                for c in range(1,len(dimen)):
                    dotl = []
                    al = []
                    for d in range(dimen[c]):
                        sum = 0
                        for e in range(dimen[c-1]):
                            sum+=weights[c-1][e][d]*avals[c-1][e]
                        dotl.append(sum+bvals[c][d])
                    for f in dotl:
                        al.append(A(f))
                    dotvals.append(dotl)
                    avals.append(al)
                ndelta = []
                for g in range(dimen[len(dimen)-1]):
                    ndelta.append(Aprime(dotvals[len(dotvals)-1][g])*(nose[1]-avals[len(avals)-1][g]))
                deltavals.append(ndelta)
                for h in range(len(dimen)-2,-1,-1):
                    ndelta = []
                    for l in range(dimen[h]):
                        sum = 0
                        for m in range(dimen[h+1]):
                            sum+=weights[h][l][m]*deltavals[len(dimen)-h-2][m]
                        ndelta.append(Aprime(dotvals[len(dotvals)-1][g])*sum)
                    deltavals.append(ndelta)
                deltavals.reverse()
                for p in range(len(dimen)-1):
                    for q in range(dimen[p]):
                        for r in range(dimen[p+1]):
                            weights[p][q][r]+=lamb*avals[p][q]*deltavals[p+1][r]
                for t in range(len(dimen)-1):
                    for s in range(dimen[t+1]):
                        bvals[t+1][s]+= lamb*deltavals[t+1][s]
                overallavals.append(avals)
                # print("delta: ", deltavals)
                # print("A: ", avals)
                # print("dot: ", dotvals)
                # print("bias: ",bvals)
                # print(weights)
                # print("-------------------------------------------------------------------------")
        error = 0
        for tiffin in range(len(overallavals)):
            error+=(overallavals[tiffin][len(dimen)-1][0]-trainingset[tiffin][1])**2
        cnt+=1
    print(cnt)
    return overallavals
def printmatrix(m):
    print('\n'.join(['\t'.join(['{:4}'.format(item) for item in row]) for row in m]))
final = backprop([[(0,0),0],[(0,1),1],[(1,0),1],[(1,1),0]],[2,2,1],11)
print(final)
# for v in range(len(final)):
#     print("Level "+str(v)+" Weight Matrix")
#     printmatrix(final[v])
#     print()
#print(final)
