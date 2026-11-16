'''
Author: 杜泽瑞
Email: 1076299954@qq.com
Date: 2026-11-11 12:50:45
Description: 字典操作示例
'''
from copy import deepcopy
# 不可变对象：int、float、bool、str、tuple
# 可变对象：list、dict、set
# 重点坑：元组里面如果放列表，**元组本身不可变，但里面的列表是可变的**
'''#浅拷贝互相影响的前提：
#拷贝出来的新容器里，有可变对象list 列表，dict 字典，set 集合。并且你修改这个可变对象内部内容，而不是重新赋值覆盖键！'''
score = {'张三': 100, '李四': 89, '王武': 333}
score1 = score.copy()  
score1['张三'] = 99  
score1.update({'小明': 100, '小红': 99}) # 新增的键 不会影响原来的字典
score2 = deepcopy(score)  # 深度复制只修改副本的值,永远互不干扰
score2.update({'cccc': 100, 'fffff': 99})
# score.clear()
print("score:", score)
print("score1:", score1)
print("score2:", score2)
'''会一起变的正确浅拷贝的例子，'''
phonebook ={'bbb': [13812345678], 'aaa': [13812345555678], 'ccc': [13812345678]}
phonebook1 = phonebook.copy()
phonebook1['bbb'].append(111111111)
print("phonebook:", phonebook)
print("phonebook1:", phonebook1)
# get获取字典元素
print("get获取字典元素",score.get("张三"))
# 判断key是否存在于字典
print('判断key是否存在于字典','张三' in score)
score['李四'] = 22222
print(score['李四'])
# score.clear() 清空字典
# 使用keys方法获得key值
key1 = score.keys()
print('使用keys方法获得key值',key1)
# 以列表形式输出
print('以列表形式输出',list(key1))
# 用values的方法获得value值
value1 = score.values()
print('用values的方法获得value值',value1)
print(list(value1))
# 使用items的方法获得key和value值
score1 = score.items()
print('使用items的方法获得key和value值',score1)
print(list(score1))
'''dict.fromkeys()
类方法，**用来快速新建字典**，把可迭代对象里的元素全部作为 key，所有 key 绑定同一个 valuePython
常见可迭代对象：列表、元组、字符串、字典、集合等
不可迭代对象：int、float、bool、None 等
'''
keys = ["张三","李四","王五"] # 不给value，默认是None
d = dict.fromkeys(keys)
# {'张三': None, '李四': None, '王五': None}
print(d)
d1 = dict.fromkeys(keys, 100) # 给value，默认是100
print(d1)
# {'张三': 100, '李四': 100, '王五': 100}
for k in d:   # 等价于 for k in d.keys()
    print(k)
# d.values()、d.items() 也都是可迭代对象
a = dict.fromkeys(["b","c"], [])
print(a)
# {'a': [], 'b': []}
a["b"].append(99)
print(a)
# {'b': [99], 'c': [99]} ！！c也被改了




