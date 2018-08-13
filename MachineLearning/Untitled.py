import math
import csv
CLASS_idx = 0
def getData(file):
    global CLASS_idx
    header=[]
    with open(file) as infile:
        reader = csv.reader(infile)
        for row in reader:
            header = row
            break
        ds={row[0]:row[1:] for row in reader}
    CLASS_idx = len(header)-1
    return ds,header
def val_list(data,column):
    return [val[column] for val in data.values()]
def val_set(data,column):
    return set(val_list(data,column))
def extract(data,column,value):
    return {a:data[a] for a in data if data[a][column] == value}
def freq_dist(data_dict):
    vals = val_list(data_dict,CLASS_idx)
    return {a:vals.count(a) for a in set(vals)}
def freq_entropy(freq_dist):
    f=list(freq_dist.values())
    s=sum(f)
    p=[i/s for i in f]
    return (-sum([i*math.log(i,2) for i in p if i>0]))
def param_entropy(data,col):
    length=len(data)
    total=0
    for v in val_set(data,col):
        ds=extract(data,col,v)
        l=len(ds)
        e=freq_entropy(freq_dist(ds))
        total+=l/length*e
    return total
def make_tree(ds):
    best = min(param_entropy(ds,i),i) for i in range(CLASS_idx)
    p = best[1]
    print("---"*level,header[p],"?")
    for v in val_set(ds):
        new_ds=extract(ds,p,v)
        freqs=freq_ds(new_ds)
        if freq_entropy(freqs)<0.001:
            print("---"*level+">",v, new_ds.values()[0][CLASS_idx])
        else:
            print("---"*level+"> "+v)
make_tree(getData("cook.csv")[0],1)
    

        

    
