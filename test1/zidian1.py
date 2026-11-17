'''
Author: 杜泽瑞
Email: 1076299954@qq.com
Date: 2026-11-16 12:17:14
Description: 
'''
# 遍历字典
score = {'张三': 100, '李四': 89, '王武': 333}
for item in score:
    print(item, score[item], score.get(item))
item1 = ['fruits', 'books', 'others']
price1 = [22, 33, 44, 445, 4455]
'''创建字典的主要方法：
1.使用大括号{} 2.使用dict()函数 3.使用fromkeys()类方法 4.使用字典推导式'''
#1 使用大括号{}创建字典
d = {'fruits': 22, 'books': 33, 'others': 44}
print(d)
#2 使用dict()函数创建字典
d = dict(name="张三", age=30)
print('使用dict()函数创建字典:',d)
# 2 使用dict()函数创建字典  两个列表合并成字典
d = dict(zip(item1, price1))
print("使用dict()函数创建字典  两个列表合并成字典:",d)
#3 使用fromkeys()类方法创建字典 批量建“同值”字典
d = dict.fromkeys(item1, 100)
print('fromkeys()类方法创建字典 批量建“同值”字典:',d)
#4 使用字典推导式创建字典
d = {item: price for item, price in zip(item1, price1)}
print('使用字典推导式创建字典:',d)    
# 使用字典推导式创建字典  将key转换成大写
d = {item.upper(): price for item, price in zip(item1, price1)}
print('字典推导式创建字典  将key转换成大写:',d)
print(type(d))
