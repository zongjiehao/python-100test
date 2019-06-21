from sys import stdout
def output(s,l):
    if l == 0:
        return
    else:
        stdout.write(s[l-1])
        output(s,l-1)


s = input("请输入一个字符串:")
l = len(s)
output(s,l)

a = input("请属于一个五位数:")
for i in range(int(len(a))):
    print(a[-i-1],end="")
