score = {'张三': 100, '李四': 89, '王武': 333}
# score['小明'] = 9999
print(score)
# get获取字典元素
print(score.get("张三"))
# 判断key是否存在于字典
print('张三' in score)
score['李四'] = 22222
print(score['李四'])
#   score.clear() 清空字典
# 使用keys方法获得key值
print(score)
key1 = score.keys()
print(key1)
# 以列表形式输出
print(list(key1))
# 用values的方法获得value值
value1 = score.values()
print(value1)
print(list(value1))
# 使用items的方法获得key和value值
score1 = score.items()
print(score1)
print(list(score1))
