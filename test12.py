# encoding:utf-8
# author:haozj 
# create_time: 2019/6/19
from math import sqrt

count = 0
flag = 1
for i in range(101, 20100):
    mid = int(sqrt(i))
    for j in range(2, mid+1):
        if (i % j == 0):
            flag = 0
            break
    if flag == 1:
        print(i)
        count += 1
    flag = 1
print(count)
