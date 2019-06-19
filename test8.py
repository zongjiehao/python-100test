# 输出 9*9 乘法口诀表。
for i in range(1, 10):
    for j in range(1, i + 1):
        print("%d*%d=%2d" % (i, j, i * j), end=" ")
    print("")

print("\n".join('\t'.join('{}*{}={}'.format(j, i, j * i) for j in range(1, i + 1)) for i in range(1, 10)))
