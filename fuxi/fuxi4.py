a = ['h', 'a', 'p', 'p', 'y']
a.sort()
a.reverse()
a.remove('p')
# print(a.sort())
print(sorted(a))
print(a, type(a))
b = 'h', 'a', 'p', 'p', 'y'
print(b, type(b))
c = 'b',
print(c, type(c))
format1 = "hellow,%s ,%s enough for ya?"
values1 = ('world', 'hot')
print(format1 % values1)
from math import e

# pi = 3.1415926
print('{:010.2f}'.format(e))
q = 'Hellow'
w = 'world'
print(q.ljust(6, '\\'))  # ljust的使用
print(q.rjust(8, '|'))  # rjust的使用
print(q.center(50))  # center的使用
print(q.find('l'))  # find的使用
print(q.rfind('l'))  # rfind的使用
print(w.join(q))  #  join的使用
print(q.split('e')) # split的使用
print(q.lower())  # lower的使用
print(q.upper())  # upper的使用

