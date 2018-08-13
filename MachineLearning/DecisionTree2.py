import math
import csv
import random
import matplotlib.pyplot as plt

CLASS_idx = 0
NODE_COUNT = 0
qcount = 0

class Node:
    def __init__(self, value, children):
        self.value = value
        self.children = children


def getData(file):
    global CLASS_idx
    header = []
    with open(file) as infile:
        reader = csv.reader(infile)
        for row in reader:
            header = row
            break
        header = header[1:]
        ds = {row[0]: row[1:] for row in reader}

    CLASS_idx = len(header) - 1
    return ds, header


def val_list(data, column):
    return [val[column] for val in data.values()]


def val_set(data, column):
    return set(val_list(data, column))


def extract(data, column, value):
    return {a: data[a] for a in data if data[a][column] == value}


def freq_dist(data_dict):
    vals = val_list(data_dict, CLASS_idx)
    return {a: vals.count(a) for a in set(vals)}


def freq_entropy(freq_dist):
    f = list(freq_dist.values())
    s = sum(f)
    p = [i / s for i in f]
    v = (-sum([i * math.log(i, 2) for i in p if i > 0]))
    return v


def param_entropy(data, col):
    length = len(data)
    total = 0
    for v in val_set(data, col):
        ds = extract(data, col, v)
        l = len(ds)
        e = freq_entropy(freq_dist(ds))
        total += l / length * e
    return total


def build_tree(ds, header, level):
    global NODE_COUNT
    best = min((param_entropy(ds, i), i) for i in range(CLASS_idx))
    p = best[1]
    curr = Node(header[p], [])
    NODE_COUNT +=1
    for n in val_set(ds, p):
        #NODE_COUNT+=1
        child = Node(n, [])
        curr.children.append(child)
    for v in curr.children:
        new_ds = extract(ds, p, v.value)
        freqs = freq_dist(new_ds)
        if freq_entropy(freqs) < 0.001:
            val = "" + list(freqs.keys())[0]
            v.children = [Node(val, [])]
        else:
            v.children.append(build_tree(new_ds, header, level + 1))
    return curr


def traverse(ds, row, tree, headers):
    global qcount
    node = tree
    while True:
        curr_val = node.value
        if len(node.children) == 0:
            return curr_val
        mychilds = node.children
        if curr_val in headers:
            name = row[headers.index(curr_val)]
            if name == '?':
                #return "Saiteej"
                pos = val_list(ds, headers.index(curr_val))
                freq = {a: pos.count(a) for a in set(pos)}
                #print(freq)
                if int(freq['y']) > int(freq['n']):
                    name = 'y'
                else:
                    name = 'n'
                # if int(freq['Sometimes']) > int(freq['Always']) and int(freq['Sometimes']) > int(freq['Never']):
                #     name = 'Sometimes'
                # if int(freq['Always']) > int(freq['Sometimes']) and int(freq['Always']) > int(freq['Never']):
                #     name = 'Always'
                # if int(freq['Never']) > int(freq['Sometimes']) and int(freq['Never']) > int(freq['Always']):
                #     name = 'Never'
                # else:
                #     qcount+=1
                #     return 'True'
            for i in mychilds:
                if i.value == name:
                    node = i
        else:
            node = mychilds[0]
    return node


def make_tree(ds, header, level):
    best = min((param_entropy(ds, i), i) for i in range(CLASS_idx))
    p = best[1]
    print("---" * level, header[p], "?")
    for v in val_set(ds, p):
        new_ds = extract(ds, p, v)
        freqs = freq_dist(new_ds)
        if freq_entropy(freqs) < 0.001:
            print("---" * level + ">", v, list(freqs.keys())[0])
        else:
            print("---" * level + "> " + v)
            make_tree(new_ds, header, level + 1);


def graph(file):
    global NODE_COUNT
    data = getData(file)
    ds = data[0]
    headers = data[1]
    values = list(ds.values())
    percents = []
    size = list(range(10,200,10))
    for s in size:
        NODE_COUNT=0
        curr_p = []
        node_counts = []
        for o in range(100):
            NODE_COUNT = 0
            done = []
            tree_data = {}
            for i in range(s):
                tree_data[i] = random.choice(values)
                while '?' in tree_data[i] or tree_data[i] in done:
                    tree_data[i] = random.choice(values)
                done.append(tree_data[i])
            tree = build_tree(tree_data, headers, 1)
            node_counts.append(NODE_COUNT)
            correct_count = 0
            wrong_count = 0
            for d in ds.values():
                if d not in tree_data.values():
                    ans = traverse(ds, d, tree, headers)
                    if ans == d[len(d) - 1]:
                        correct_count += 1
                    else:
                        wrong_count += 1
            p = (correct_count/(correct_count+wrong_count))*100
            curr_p.append(p)
        avgp = sum(curr_p)/len(curr_p)
        avgnodes = sum(node_counts)/len(node_counts)
        #print(str(s) + "\t" + str(avgnodes))
        print(str(s) + "\t" + str(avgp))
        percents.append(avgp)
    print(percents)
    #plt.plot(size,percents)
    #plt.show()

def graphtwo(train,test):
    traindata = getData(train)
    testdata = getData(test)
    dstrain = traindata[0]
    dstest = testdata[0]
    headers = testdata[1]
    percents = []
    curr_p = []
    node_counts = []
    for o in range(1):
        tree = build_tree(dstrain, headers, 1)
        make_tree(dstrain, headers, 1)
        node_counts.append(NODE_COUNT)
        correct_count = 0
        wrong_count = 0
        for d in dstest.values():
            ans = traverse(dstest, d, tree, headers)
            if ans == d[len(d) - 1]:
                correct_count += 1
            else:
                wrong_count += 1
        p = (correct_count/(correct_count+wrong_count))
        print(p)
        curr_p.append(p)
    avgp = sum(curr_p)/len(curr_p)
    avgnodes = sum(node_counts)/len(node_counts)
    #print(str(s) + "\t" + str(avgnodes))
    print(avgp)
    print(NODE_COUNT)
#graphtwo("quizB_train.csv", "quizB_test_b.csv")
graph("house-votes-84.csv")


