# 遍历字典
score = {'张三': 100, '李四': 89, '王武': 333}
for item in score:
    print(item, score[item], score.get(item))
item1 = ['fruits', 'books', 'others']
price1 = [22, 33, 44, 445, 4455]
# 创建字典
d = {item.upper(): price for item, price in zip(item1, price1)}
print(d)
print(type(d))
