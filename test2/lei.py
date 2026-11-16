class Student:
    native_pace = '吉林'  # 直接写在类里的变量，称为类属性

    def __init__(self, name, age):
        self.name = name  # 实体属性，进行一个赋值操作，将局部变量的name的值赋给实体属性
        self.age = age

    # 实例方法
    def eat(self):
        print('学生在吃饭')

    # 静态方法
    @staticmethod
    def method():
        print('我是静态方法，因为我使用了 staticmethod 进行修饰')

    # 类方法
    @classmethod
    def cm(cls):
        print('我是类方法，因为我使用了 classmethod 进行修饰')


def method():
    print('我使用了staticmethod进行修饰，所以我是静态方法')


# 在类之外定义的称为函数，在类之外定义的称为方法
def drink():
    print('喝水')


# 创建Student类的值
stu1 = Student('张三', 34)
print(id(stu1))
print(type(stu1))
print(stu1)
# print('----------')
# print(id(Student))
# print(type(Student))
# print(Student)
stu1.eat()  # 对象名.方法名（）
print(stu1.age, stu1.name)
Student.eat(stu1)  # 类名.方法名（类的对象）实际就是方法定义处的self

#  类属性的使用方式
print(Student.native_pace)
Student.native_pace = '天津'
print(stu1.native_pace)
print('静态方法与类方法的使用')
Student.cm()
Student.method()
stu1.cm()
stu1.method()
