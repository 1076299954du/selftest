"""常用排序算法集合。

所有排序方法都按升序排序，并且直接在传入的列表上原地修改，
同时返回该列表，方便链式调用或直接打印结果。
"""

from typing import List, TypeVar

T = TypeVar("T")


class Sort:
    """封装冒泡、选择、插入、快速、归并和堆排序。"""

    @staticmethod
    def bubble_sort(nums: List[T]) -> List[T]:
        """冒泡排序（原地升序）。

        时间复杂度：最好 O(n)，平均/最坏 O(n^2)
        空间复杂度：O(1)
        稳定排序：是
        """
        n = len(nums)
        for i in range(n - 1):
            swapped = False
            # 每轮结束后，末尾的 i + 1 个元素已经有序
            for j in range(n - 1 - i):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    swapped = True
            if not swapped:
                break
        return nums

    @staticmethod
    def selection_sort(nums: List[T]) -> List[T]:
        """选择排序（原地升序）。

        时间复杂度：最好/平均/最坏 O(n^2)
        空间复杂度：O(1)
        稳定排序：否
        """
        n = len(nums)
        for i in range(n - 1):
            min_index = i
            for j in range(i + 1, n):
                if nums[j] < nums[min_index]:
                    min_index = j
            if min_index != i:
                nums[i], nums[min_index] = nums[min_index], nums[i]
        return nums

    @staticmethod
    def insertion_sort(nums: List[T]) -> List[T]:
        """插入排序（原地升序）。

        时间复杂度：最好 O(n)，平均/最坏 O(n^2)
        空间复杂度：O(1)
        稳定排序：是
        """
        for i in range(1, len(nums)):
            current = nums[i]
            j = i - 1
            # 比 current 大的元素依次后移，为 current 腾出位置
            while j >= 0 and nums[j] > current:
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = current
        return nums

    @staticmethod
    def quick_sort(nums: List[T]) -> List[T]:
        """快速排序（原地升序，双指针分区）。

        时间复杂度：平均 O(n log n)，最坏 O(n^2)
        空间复杂度：O(log n)（递归栈）
        稳定排序：否
        """
        Sort._quick_sort(nums, 0, len(nums) - 1)
        return nums

    @staticmethod
    def _quick_sort(nums: List[T], low: int, high: int) -> None:
        """对 nums[low:high + 1] 进行快速排序。"""
        if low >= high:
            return

        pivot = nums[(low + high) // 2]
        left, right = low, high

        while left <= right:
            while nums[left] < pivot:
                left += 1
            while nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        Sort._quick_sort(nums, low, right)
        Sort._quick_sort(nums, left, high)

    @staticmethod
    def merge_sort(nums: List[T]) -> List[T]:
        """归并排序（原地升序）。

        时间复杂度：最好/平均/最坏 O(n log n)
        空间复杂度：O(n)
        稳定排序：是
        """
        nums[:] = Sort._merge_sort(nums)
        return nums

    @staticmethod
    def _merge_sort(nums: List[T]) -> List[T]:
        """返回 nums 排序后的新列表。"""
        if len(nums) <= 1:
            return nums[:]

        mid = len(nums) // 2
        left = Sort._merge_sort(nums[:mid])
        right = Sort._merge_sort(nums[mid:])
        return Sort._merge(left, right)

    @staticmethod
    def _merge(left: List[T], right: List[T]) -> List[T]:
        """合并两个已排序的列表，保持稳定性。"""
        merged: List[T] = []
        i = j = 0

        while i < len(left) and j < len(right):
            # 相等时先取左侧元素，保证稳定排序
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged

    @staticmethod
    def heap_sort(nums: List[T]) -> List[T]:
        """堆排序（原地升序，使用大顶堆）。

        时间复杂度：最好/平均/最坏 O(n log n)
        空间复杂度：O(1)
        稳定排序：否
        """
        n = len(nums)

        # 从最后一个非叶子节点开始，自下而上建大顶堆
        for i in range(n // 2 - 1, -1, -1):
            Sort._sift_down(nums, i, n)

        # 每次把堆顶（当前最大值）换到末尾，再调整剩余部分
        for end in range(n - 1, 0, -1):
            nums[0], nums[end] = nums[end], nums[0]
            Sort._sift_down(nums, 0, end)

        return nums

    @staticmethod
    def _sift_down(nums: List[T], root: int, size: int) -> None:
        """在 nums[0:size] 这个大顶堆中，将 root 向下调整到合适位置。"""
        while True:
            child = 2 * root + 1
            if child >= size:
                break

            # 选择左右孩子中较大的一个
            if child + 1 < size and nums[child + 1] > nums[child]:
                child += 1

            if nums[root] >= nums[child]:
                break

            nums[root], nums[child] = nums[child], nums[root]
            root = child


if __name__ == "__main__":
    original = [64, 34, 25, 12, 22, 11, 90]
    methods = (
        "bubble_sort",
        "selection_sort",
        "insertion_sort",
        "quick_sort",
        "merge_sort",
        "heap_sort",
    )

    print(f"原始数据：{original}")
    for method_name in methods:
        data = original.copy()
        getattr(Sort, method_name)(data)
        print(f"{method_name:<15}: {data}")
