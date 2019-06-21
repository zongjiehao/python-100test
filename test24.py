from functools import reduce

a = 2
b = 1
L = []
L.append(a / b)
for i in range(1, 20):
    b, a = a, a + b
    L.append(a / b)

print(reduce(lambda x, y: x + y, L))
