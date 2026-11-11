class Student:
    native_pace = '吉林'

    # """直接写在类里的变量，称为类属性"""

    def __init__(self, name, age):  # Student为类的名称（类名）由一个或多个单词组成，每个单词的首字母大写，其余小写
        self.name = name
        self.age = age

    """实例方法"""

    def eat(self):
        print("""学生正在吃饭""")
        # return

    """静态方法"""

    @staticmethod
    def method():
        print("""我使用了staticmethod,所以我是静态方法""")

    """类方法"""

    @classmethod
    def cm(cls):
        print("""我使用了classmethod,所以我是类方法""")


def drink():
    print("喝水")


stu = Student("jed", 89)
print("````````````")
stu.eat()
Student.eat(stu)
"""35和36实现的是同一个功能。两种方式"""
# # drink()
# # print(id(stu))
# # print(type(stu))
# # print(stu)
# print("============")
# print(stu.name)
# print(stu.age)
