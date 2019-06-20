from functools import reduce
journy =[]
height = 100
time = 10
for i in range(1,11):
    if i==1:
        journy.append(height)
    else:
        journy.append(height*2)
    height = height/2
print(height)
print(reduce(lambda x,y:x+y,journy))

