from functools import reduce
def sum(a, b):
    return a + b

for i in range(2,1000):
    L=[1]
    for j in range(2,int(i/2+1)):
        if i % j ==0:
            L.append(j)
    if i == reduce(sum,L):
        print(i)
        print(L)

