'''
Author: 杜泽瑞
Email: 1076299954@qq.com
Date: 2026-11-05 14:02:37
Description: 
'''
lst = [1,2,3]
print(lst)
lst.pop(0)
print("888",lst.pop(1))
lst[1:1]=[2,2.5]
lst.append(4)
print(lst)
a = lst
b = a.copy()
b[2:]=[3,4,5]
b.extend([6,7,8])
print("a:",a)
print("b:",b)
print("a+b:",a+b)
a = a+b
print("a:",a)

print("dd")
