# 选择排序（Selection Sort）
#
# 基本思路：
#   每一轮在未排序的部分中找到最小（或最大）的元素，
#   把它放到未排序部分的最前面，然后缩小未排序的范围，
#   重复直到整个列表有序。
#
# 以 [2, 6, 1] 为例：
#   第 1 轮：在 [2, 6, 1] 中找最小值 1，与第 1 个元素 2 交换 -> [1, 6, 2]
#   第 2 轮：在 [6, 2] 中找最小值 2，与 6 交换           -> [1, 2, 6]
#
# 时间复杂度：O(n^2)（无论数据是否有序，比较次数都一样）
# 空间复杂度：O(1)（原地排序，只需常数个额外变量）
# 稳定性：不稳定（交换可能破坏相等元素的相对顺序）
# 特点：交换次数少，最多 n-1 次交换。


def selection_sort(arr):
    """对列表 arr 做升序选择排序，原地修改并返回该列表。"""
    n = len(arr)

    # 一共需要 n-1 轮；每轮确定一个位置上的元素
    for i in range(n - 1):
        # 先假设未排序部分的第一个元素就是最小的
        min_index = i

        # 在剩下的元素中寻找更小的元素，记录其下标
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # 如果最小元素不在当前位置，才交换（减少无谓的交换）
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


def selection_sort_desc(arr):
    """对列表 arr 做降序选择排序（每轮找最大值），原地修改并返回该列表。"""
    n = len(arr)

    for i in range(n - 1):
        max_index = i
        for j in range(i + 1, n):
            if arr[j] > arr[max_index]:
                max_index = j
        if max_index != i:
            arr[i], arr[max_index] = arr[max_index], arr[i]

    return arr


if __name__ == "__main__":
    # 基本演示
    data = [2, 6, 1, 7, 89, 34, 777]
    print("排序前：", data)
    print("升序后：", selection_sort(data[:]))  # 传入副本，保留原列表
    print("降序后：", selection_sort_desc(data[:]))

    # 边界情况测试
    print("-" * 30)
    print("空列表：", selection_sort([]))
    print("单元素：", selection_sort([5]))
    print("已有序：", selection_sort([1, 2, 3, 4, 5]))
    print("全相同：", selection_sort([3, 3, 3]))
    print("含负数：", selection_sort([0, -3, 8, -1, 8]))
