a = input("请属于一个五位数:")
flag = 1
for i in range(int(len(a)/2)):
    if a[i] != a[-i-1]:
        flag=0
        break

if flag==1:
    print("%s是个回文数"%a)
else:
    print("%s不是个回文数"%a)



