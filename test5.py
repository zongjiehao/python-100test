# 输入三个整数x,y,z，请把这三个数由小到大输出。
l=[]
for i in range(3):
    x=input("整数:\n")
    l.append(x)
l.sort()
print(l)