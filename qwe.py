# 学习输出数字，表达式，字符串
print(5665656)
print(3 + 3)
# 不换行输出，中间用'，'隔开
print('bobby', 'ddd')
print('hello\nworld')
print('hello\tworld')
print('hello\tworld')
print('hello\rworld')
print('hello\bworld')
# 算数运算符
print(-9 // 4)
print(-9 % 4)
# 计算1到100之间偶数的和
sun = 0
print(sun)
i = 1
while i <= 100:
    if i % 2 == 0:
        sun += i
    i = i + 1
print('输出和', sun)
# 用for计算1到100之间偶数的和
he = 0
for item in range(1, 101):
    if item % 2 == 0:
        he += item

print('输出的和是', he)
