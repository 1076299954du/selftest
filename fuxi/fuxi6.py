# eval函数与exec函数
dic = {}  # 定义一个字典
dic['b'] = 3  # 在 dic 中加一条元素，key 为 b
print(dic)
print(dic.keys())  # 先将 dic 的 key 打印出来，有一个元素 b
exec("a = 4", dic)  # 在 exec 执行的语句后面跟一个作用域 dic
#  print(dic)
print(dic.keys())  # exec 后，dic 的 key 多了一个

a = 10
b = 20
c = 30
g = {'a': 6, 'b': 8}  # 定义一个字典
t = {'b': 100, 'c': 10}  # 定义一个字典
print(eval('a+b+c', g, t))  # 定义一个字典 116
