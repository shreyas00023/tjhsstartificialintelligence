import numpy as np
def length(x):
    return x[0]**2+x[1]**2
def f(arr):
    (x,y) = arr
    #return 4*x**2-3*x*y+2*y**2+24*x-20*y
    return (1-y)**2+100*(x-y**2)**2
def find_min(func, a, b, e):
    while abs(a - b) > e:
        c = (b - a) / 3 + a
        d = b - (b - a) / 3
        if func(c) < func(d):
            b = d
        else:
            a = c
    return a
def gradient(x,y):
    #return np.array([(8*x)-(3*y)+24,(-3*x)+(4*y)-20])
    return np.array([(200*x)-200*(y**2),-400*y*(x-y**2)+2*y-2])
def min_f_dynamic(func, gradient, a,b,e):
    x = np.array([a,b])
    cnt = 0
    lamb=0
    while length(gradient(x[0],x[1]))>e:
        cnt+=1
        #print(x)
        lamb = find_min(lambda l: f(x-l*gradient(x[0],x[1])),0,100,e)
        x = x-(lamb*gradient(x[0],x[1]))
    return x,cnt
def min_f(func, gradient, a,b,e,lamb):
    x = np.array([a,b])
    cnt = 0
    while length(gradient(x[0],x[1]))>e:
        cnt+=1
        #print(x)
        #lamb = find_min(lambda l: f(x-l*gradient(x[0],x[1])),0,1,e)
        x = x-(lamb*gradient(x[0],x[1]))
    return x
# def lamb(f, x,gradient,a,b):
#     return find_min(x-l*gradient(x[0],x[1]),)
# def lambfunc(l,x,gradient):
#     return x-l*gradient(x[0],x[1])
minlamb = 0
minoutput = 100000000
# for i in np.arange(0.001,0.2,.0005):
#     output = min_f(f,gradient,0,0,10**-12,i)
#     if output<minoutput:
#         minoutput=output
#         minlamb=i
#     print(str(i)+"\t"+str(output))
# print(minlamb)
# #optimal lambda = 0.162
#optimal dynamic lambda = 0.11974
# print(min_f_dynamic(f,gradient,0,0,10**-12))
# print(min_f(f,gradient,0,0,10**-12,0.162))
# (1-y)**2+100*(x-y**2)**2
print(min_f_dynamic(f,gradient,0,1,10**-12))
#karthiccccccccccccccccc
