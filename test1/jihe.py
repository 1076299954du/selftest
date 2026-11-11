# 集合的创建
s = {333, 444, 333, 33, 4455, 66654}
print(s)
print(334 in s)
s1 = set(range(6))
print(s1)
s2 = set([0, 1, 2, 3, 4])
print(s2, type(s2))
s3 = set((0, 1, 2, 3, 4))
print(s3, type(s3))
# 定义空集合
s4 = set()
print(s4, type(s4))
s5 = {} # 这样的不是空集合，而是字典
print(s5, type(s5))
