from sys import stdout
for i in range(1,5):
    for j in range(4-i):
        print(" ",end='')
    for k in range(2*i-1):
        print("*",end='')
    print("")

for i in range(3,0,-1):
    for m in range(4-i):
        print(" ",end='')
    for n in range(2*i-1):
        print("*",end='')
    print("")



