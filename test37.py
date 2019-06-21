def bubble_sort(L):
    for i in range(len(L)):
        for j in range((len(L) - i - 1)):
            if L[j] > L[j + 1]:
                L[j], L[j + 1] = L[j + 1], L[j]
        print(L[i], end=" ")
    print("")


bubble_sort([1, 4, 2, 45, 54, 34])


def select_sort(L):
    for i in range(len(L)):
        min_index = i
        for j in range(i + 1, len(L)):
            if L[min_index] > L[j]:
                L[min_index], L[j] = L[j], L[min_index]
        print(L[min_index], end=" ")
    print("")


select_sort([1, 4, 2, 45, 54, 34])


def insert_sort(L):
    # 从第二个位置，即下标为1的元素开始向前插入
    for i in range(1, len(L)):
        # 从第i个元素开始向前比较，如果小于前一个元素，交换位置
        for j in range(i, 0, -1):
            if L[j] < L[j-1]:
                L[j], L[j-1] = L[j-1], L[j]
    print(L)

L=[1, 4, 2, 45, 54, 34]
insert_sort(L)
