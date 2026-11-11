s = 'hello,python'
s2 = 'hello,java'
print('*'.join(s2))  # 字符串的链接
print(s.join(s2))
print(s.replace('python', 'java'))  # 字符串的替换
s1 = 'hello,python,python,python'
print(s1.replace('python', 'java', 2))

name = "张三"
age = 20
print('我叫%s,今年%d岁' % (name, age))
print('我叫{0},今年{1}岁'.format(name, age))
print(f'我叫{name},今年{age}岁')
print('%10d' % 99)  # 10表示的是宽度
print('%.3f' % 3.1415926)  # .3表示的是小数点后三位
print('%10.3f' % 3.1415926)  # 一共总宽度为10，小数点后3位
d = '天涯共此时'
print(d.encode(encoding='GBK'))  # 这种编码中，一个中文占2个字符
print(d.encode(encoding='UTF-8'))  # 这种编码中，一个中文占3个字符
# 解码
byte = d.encode(encoding='GBK')
print(byte.decode(encoding='GBK'))

byte = d.encode(encoding='UTF-8')
print(byte.decode(encoding='UTF-8'))

