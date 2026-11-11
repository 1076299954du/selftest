a = 'sbbbR,hero'
b = 'sbbb'
print(a.find('R'))  # 字符串的查找，从左边开始
print(a.rfind('o'))  # 从右边开始查找
print(a > b)  # 字符串的比较
print(a, id(a))
c = a.upper()  # 将所有字母转换成大写
print(c, id(c))  # 将所有字母转换成小写
d = a.lower()
print(a.lower(), id(a.lower()))
print(d, id(d))
print('--', a.swapcase())  # 小写换大写，大写换小写
print('===', a.capitalize())  # 第一个字母大写，剩下的小写
print(a.title())  # 将每个单词的第一个大写
print('------')
q = 'hello,world python'
print(type(q))
lst = q.split(sep=",")
lst1 = q.split()
print('+++++', lst)  # 以空格来拆分
print("*****",lst1)
print(q.rsplit(sep=',', maxsplit=1)) # 以逗号来拆分
