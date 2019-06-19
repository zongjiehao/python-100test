# encoding:utf-8
# author:haozj 
# create_time: 2019/6/19
def tuzi(n):
    if n == 1 or n == 2:
        return 1
    else:
        return tuzi(n - 1) + tuzi(n - 2)

print(tuzi(22))
