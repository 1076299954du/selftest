# 选择排序
# 选择排序基本思路：
# 把第一个元素依次和后面的所有元素进行比较。
# 第一次结束后，就会有最小值出现在最前面。

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        # 假设当前位置元素最小
        min_index = i
        for j in range(i + 1, n):
            # 如果后面的元素更小，更新最小元素的下标
            if arr[j] < arr[min_index]:
                min_index = j
                # 将最小元素和当前位置元素交换位置
        # arr[i], arr[min_index] = arr[min_index], arr[i] # 用了元组解包的知识点
        temp = arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = temp
        # arr[i] = arr[min_index]
        # arr[min_index] = arr[i]
    return arr


# 冒泡排序
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            # 如果当前元素大于下一个元素，交换它们的位置
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# 快速排序   以第一个元素作为基准元素，将原数组分为2块
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = []
        right = []
        for i in arr[1:]:
            if i < pivot:
                left.append(i)
            else:
                right.append(i)
        return quick_sort(left) + [pivot] + quick_sort(right)


# 插入排序
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            arr[j + 1] = key
    return arr


# 希尔排序
def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
                arr[j] = temp
                print(arr)
        gap //= 2
    return arr


print(selection_sort([2, 6, 1, 7, 89, 34, 777]))
print(bubble_sort([2, 6, 1, 7, 888, 89, 34, 777]))
print(quick_sort([2, 6, 1, 7, 888, 89, 34, 777]))
print(insertion_sort([2, 6, 1, 7, 888, 89, 34, 777]))
print(shell_sort([2, 6, 1, 7, 888, 89, 34, 777, 8888]))
