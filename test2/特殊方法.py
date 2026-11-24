'''
Author: duzerui
Date: 2026-11-16 11:22:52
LastEditors: duzerui
LastEditTime: 2026-11-24 18:00:00
Description: 文件功能描述
'''

class Student:
    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        return self.name + other.name

    def __len__(self):
        return len(self.name)


stu1 = Student('张三')
stu2 = Student('lisi')
s = stu1 + stu2  # 实现了两个对象的加法运算（因为在Studet类中，编写__add__()特殊方法，使自定义对象具有'+'的功能）
print(s)
print(len(stu2))  # 通过重写内置函数len()，使内置函数len()的参数可以是自定义类型

class FooBar:
    def __init__(self, value=42):
        self .somevar = value
f = FooBar('This is a constructor argument')
print(f.somevar)  # This is a constructor argumen