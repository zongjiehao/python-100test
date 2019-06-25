def bubble_sort(L):
    for i in range(0, len(L) - 1):
        for j in range(0, len(L) - i - 1):
            if L[j] > L[j + 1]:
                L[j], L[j + 1] = L[j + 1], L[j]
    print(L)


#bubble_sort([1, 4, 2, 45, 54, 34])


def bubble_sort_optimize(l):
    for i in range(len(l) - 1):
        is_sort = True
        for j in range(len(l) - 1 - i):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
                is_sort = False
        if is_sort:
            break
    print(l)


#bubble_sort_optimize([1, 4, 2, 45, 54, 34])



def select_sort(L):
    for i in range(len(L)):
        min_index = i
        for j in range(i + 1, len(L)):
            if L[min_index] > L[j]:
                L[min_index], L[j] = L[j], L[min_index]
    print(L)


select_sort([1, 4, 2, 45, 54, 34])


def insert_sort(L):
    # 从第二个位置，即下标为1的元素开始向前插入
    for i in range(1, len(L)):
        # 从第i个元素开始向前比较，如果小于前一个元素，交换位置
        for j in range(i, 0, -1):
            if L[j] < L[j - 1]:
                L[j], L[j - 1] = L[j - 1], L[j]
    print(L)


L = [1, 4, 2, 45, 54, 34]
# insert_sort(L)
