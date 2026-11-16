class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def show(self):
        print(self.name, self.__age)


stu = Student('张三', 20)
stu.show()
# 在类的外部使用name和age
print(stu.name)
"""会报错"""
# print(stu.__age)

print(dir(stu))
print(stu._Student__age)  # 在类的外部可以通过这种方式强行访问

