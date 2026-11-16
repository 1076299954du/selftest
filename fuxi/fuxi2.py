tag = 'https://www.bilibili.com/'
number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
number[0] = 90
print(number)
print(len(number))
print(max(number))
print(min(number))
q = tag[8:-1]
a = tag[1:4:2]
print(q)
print(a, type(a))
print(number[6:3:-1])
print(number[-3:]*4)
print(number[6:3:-1]+number[-3:])
print(number[0:])
print(number[:])
print(88 in number)
