soundrel = {'name': 'Robin', 'girlfrend': 'Marion'}
key, value = soundrel.popitem()
print(key)
print(value)
a, *b, c = "abc"  # 带*号的变量一定是个列表
print(a, b, c)
x = y = [1, 2, 3]
z = [1, 2, 3]
print('x:', id(x))
print('y:', id(y))
print('z:', id(z))
print(x == y)
print(x == z)
print(x is y)
print(x is z)
