def fn(n):
    sum = 0
    if n == 0:
        return 1
    else:
        sum = n * fn(n-1)
    return sum

print(fn(5))
