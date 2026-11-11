lst = list([555, 505, 667, 333, 78768])
print(lst)
lst.append(888)
#lst.insert(2, 'gg')
print(lst)
list1 = lst[1:]
lst.sort(reverse=True)
print(lst)
print(type(lst))
lst1 = [i * 2 for i in range(1, 6)]
print(lst1)
student = dict(name='jack', age=20)
print(student)
