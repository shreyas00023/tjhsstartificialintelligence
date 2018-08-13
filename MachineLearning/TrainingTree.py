import math
def entropy(vector):
    yes = vector[0]
    no = vector[1]
    total = yes+no
    if yes==0 or no==0:
        return 0
    entropy = -((yes/total)*math.log((yes/total),2)+(no/total)*math.log((no/total),2))
    return entropy
def avgentropy(biglist):
    sume = 0
    totsum = 0
    for n in biglist:
        totsum = totsum+n[0]+n[1]
    for i in biglist:
        sume = sume+(((i[0]+i[1])/totsum)*entropy(i))
    return sume
##while True:
##    x = int(input("yes: "))
##    y = int(input("no: "))
##    print(entropy([x,y]))
blist = [3,2]
print(entropy(blist))
    

    
