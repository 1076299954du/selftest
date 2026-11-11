class Student:
    def __init__(self, name, age):
        self.name = name  # 实体属性，进行一个赋值操作，将局部变量的name的值赋给实体属性
        self.age = age

    def eat(self):
        print(self.name + '在吃饭')


stu1 = Student('张三', 33)
stu2 = Student('李四', 99)
print(id(stu1))
print(id(stu2))
print('----为stu1动态绑定性别属性-----')
stu1.gender = '女'
print(stu1.name, stu1.age, stu1.gender)


def show():
    print("定义在类之外的称函数")


# 动态绑定方法
stu1.show = show
stu2.show = show
stu2.show()
stu1.show()
