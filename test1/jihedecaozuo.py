s = {333, 444, 33, 4455, 66654}
s1 = {333, 444, 545}
# 交集操作
print(s1.intersection(s))
print(s1 & s)
# 并集操作
print(s1.union(s))
print(s1 | s )
# 差集操作
print(s.difference(s1))

print(s1.isdisjoint(s))  # 判断2个集合之间是否存在交集
s.add(100)
print(s)
s.update((44,))  # 元素的添加操作
s.update([44, 55])
s.update({49, 59})
s.remove(33)  # 元素的移除操作
print(s)
# 集合生成式 无序
s2 = {i*8 for i in range(1, 10)}
# 列表生成式 有序
s3 = [i*8 for i in range(1, 10)]
print(s2)
print(s3)
