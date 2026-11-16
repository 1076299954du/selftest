# python 的二分法

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == target:
            return mid
        if guess > target:
            high = mid - 1
        else:
            low = mid + 1
    return None


# 测试代码

my_list = [1, 3, 5, 7, 9, 67, 88]
print(binary_search(my_list, 88))
print(binary_search(my_list, 99))
