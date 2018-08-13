import math
import csv
mydic = {}
rows = []
cols = []
with open("cook.csv",newline='') as infile:
    reader = csv.reader(infile)
    for row in reader:
        rows.append(row)
    cols = rows[0]
    for c in cols:
        mydic[c] = []
    for a in cols:
        for b in range(1,len(rows)):
            mydic[a].append(rows[b][cols.index(a)])
def entropy(vector):
    cnt = 0
    total = 0
    entropy = 0
    for v in vector:
        if v==0:
            cnt = cnt+1
        total = total+v
    if cnt>(len(vector)-2):
        return 0
    for b in vector:
        entropy = entropy+math.log((b/total),2)
    return -entropy
def avgentropy(biglist):
    sume = 0
    totsum = 0
    for n in biglist:
        totsum = totsum+findSum(n)
    for i in biglist:
        sume = sume+(((findSum(i))/totsum)*entropy(i))
    return sume
def findSum(vector):
    s = 0
    for n in vector:
        s = s+n
    return s
def extract(ds,col,val):
    newdic = {}
    for c in cols:
        newdic[c] = []
    indeces = []
    for n in range(len(ds[col])):
        if ds[col][n] == val:
            indeces.append(n)
    for i in indeces:
        for z in cols:
            newdic[z].append(ds[z][i])
    return newdic
def getAnswers(ds):
    return ds[cols[len(cols)-1]]
def getFreq(ds, col, vals):
    allfreq = []
    answercol = ds[cols[len(cols)-1]]
    for v in vals:
        a = []
        thiscol = ds[col]
        for t in range(len(thiscol)):
            if thiscol[t]==v:
                a.append(answercol[t])
        freqs = {b:a.count(b) for b in set(a)}
        allfreq.append(freqs)
    return allfreq
def get_best_col(ds):
    allentropies = {}
    for col in range(1,len(cols)-1):
        valset = set(ds[cols[col]])
        freq = getFreq(ds,cols[col],valset)
        entropies = []
        for s in freq:
            entropy = []
            for j in s.keys():
                entropy.append(s[j])
            entropies.append(entropy)
        allentropies[cols[col]] = avgentropy(entropies)
    mine = 10000000000
    minname = ""
    for c in range(1,len(cols)-1):
        if allentropies[cols[c]] < mine:
            mine=allentropies[cols[c]]
            minname=cols[c]
    return minname
#print(get_best_col(extract(mydic,"Outlook","Sunny")))
def make_tree(ds, level):
    best_col = get_best_col(ds)
    print("---"*level,best_col,"?")
    for val in set(ds[best_col]):
        new_ds = extract(ds,best_col,val)
        if len(set(getAnswers(new_ds)))==1:
            print("---"*level+">",val, getAnswers(new_ds)[0])
        else:
            print("---"*level+"> "+val)
            make_tree(new_ds, level+1)
make_tree(mydic,1)

        

    
