total = 0
a = int(input('请输入几个数相加:'))
b = int(input('请输入要相加的数:'))
c=4
for i in range(a):
    total+=b
    b=b*10+c
    print(b)
print(total)


