def check_index(key):
    if not isinstance(key, int):
        raise TypeError
    if key < 0:
        raise IndexError


class ArithmeticSequence:
    def __init__(self, start=0, step=1):
        """
        初始化找个算数序列
        start 序列的第一个值
        step 两个相邻的差
        changed 一个字典，包含用户修改后的值
        """
        self.start = start
        self.step = step
        self.changed = {}  # 没有任何元素被修改

    def __getitem__(self, key):
        """从算数序列中获取一个元素"""
        check_index(key)
        try:
            return self.changed[key]
        except KeyError:
            return self.start + key * self.step

    def __setitem__(self, key, value):
        """修改算数数列中的元素"""
        check_index(key)
        self.changed[key] = value  # 存储修改后的值


s = ArithmeticSequence(1, 5)
print(s[0])
print(s[1])


class CounterList(list):
    def __init__(self, *args):
        super().__init__(*args)
        self.counter = 0

    def __getitem__(self, index):
        self.counter += 1
        return super(CounterList, self).__getitem__(index)


c = CounterList(range(10))
# c.append(10)
print(c.reverse())
print(c[3:6])
print(c)

print("计数1",c.counter)
print(c[0]+c[2])
print("计数2",c.counter)