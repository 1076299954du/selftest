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
