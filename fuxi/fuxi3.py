a = list('hellow')
# 测试append方法
a.append('!!!!')
print('a:', a, id(a), type(a))  # a: ['h', 'e', 'l', 'l', 'o', 'w', '!!!!'] 140244094658560 <class 'list'>
a[1:] = ['a', 'p', 'p', 'y']
print(a, '!!!!!!!!!!')  # ['h', 'a', 'p', 'p', 'y'] !!!!!!!!!!
d = a
print(a,)  # ['h', 'a', 'p', 'p', 'y']
# 测试insert方法
print(d)  # ['h', 'a', 'p', 'p', 'y']
d.insert(5, 'birthday')
print('****', d)  # **** ['h', 'a', 'p', 'p', 'y', 'birthday']
print("$$", a)  # $$ ['h', 'a', 'p', 'p', 'y', 'birthday']
# 测试extend方法
a.extend(a)
print('d:', d, id(d), type(d))  # d: ['h', 'a', 'p', 'p', 'y', 'birthday', 'h', 'a', 'p', 'p', 'y', 'birthday']
# 140244094658560 <class 'list'>
# 测试copy方法
c = a.copy()
print(c, id(c)) # ['h', 'a', 'p', 'p', 'y', 'birthday', 'h', 'a', 'p', 'p', 'y', 'birthday'] 140244094106496
# 测试count方法
print(d.count('p'))
# 测试index方法
print(d.index('p'))
