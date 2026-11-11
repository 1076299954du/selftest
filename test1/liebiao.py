'''
Author: 杜泽瑞
Email: 1076299954@qq.com
Date: 2026-11-11 12:50:45
Description: ()
'''
lst = list([555, 505, 667, 333, 78768])
print(lst)
lst.append(888)
#lst.insert(2, 'gg')
print("lst:",lst)
list1 = lst[1:]
print("list1",list1)
print("*****",lst)
lst.sort(reverse=False)

print("lst--",lst)
print(type(lst))
lst1 = [i * 2 for i in range(1, 6)]
print("lst1***",lst1)
student = dict(name='jack', age=20)
print("student:",student)
