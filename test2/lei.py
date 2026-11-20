'''
Author: 杜泽瑞
Email: 1076299954@qq.com
Date: 2026-11-16 12:17:14
Description: 类的学习
'''

'''class 关键字：声明这是一个类
类名：每个单词首字母大写，驼峰命名法'''
class Student:
    native_pace = '吉林'  # 写在_init_外面，属于这个类，所有对象共享。称为类属性。

    def __init__(self, name, age):
        self.name = name  # 实体属性，写在_init_里面，进行一个赋值操作，将局部变量的name的值赋给实体属性，每个对象自己独有。
        self.age = age
    '''
    - 需要操作对象数据 → 实例方法 (self)
    - 需要操作类的共享数据 → 类方法 (cls)
    - 和类、对象数据没关系，只是工具函数 → 静态方法'''
    # 实例方法：第一个参数必须是self，self代表这个类的对象本身，可以读取修改实例属性
    def eat(self):
        print('学生在吃饭')

    # 静态方法：装饰器@staticmethod，静态方法不需要传入self参数，也不需要传入cls参数，静态方法和类和对象没有关系。
    @staticmethod
    def method():
        print('我是静态方法，因为我使用了 staticmethod 进行修饰')

    # 类方法:装饰器@classmethod，类方法的第一个参数必须是cls，cls代表这个类本身，可以访问类属性，不能访问实例属性。
    @classmethod
    def cm(cls):
        print('我是类方法，因为我使用了 classmethod 进行修饰')


# 在类之外定义的称为函数，在类里面定义的称为方法
def drink():
    print('喝水')


drink()  # 函数的调用
# 创建Student类的值
stu1 = Student('张三', 34)
print('stu1的ID',id(stu1))
print('stu1的类型：',type(stu1))
print('======，打印student对象，pyton默认输出内容',stu1)
# print(id(Student))
# print(type(Student))
# print(Student)
stu1.eat()  # 对象名.方法名（）调用实例方法
print(stu1.age, stu1.name)
Student.eat(stu1)  # 类名.方法名（类的对象）实际就是方法定义处的self。调用类方法/静态方法。

#  类属性的使用方式
print(Student.native_pace)
Student.native_pace = '天津'
print(stu1.native_pace)

print('静态方法与类方法的使用')
Student.cm()
Student.method()
stu1.cm()
stu1.method()


class Dog:
    def __init__(self, name,age):
        self.name = name
        self.age = age

    def eat(self):
        print('%s爱吃骨头' % self.name)
# 创建对象，传参数给__init__方法
dog1 = Dog('大黄', 3)
dog2 = Dog('二黄', 4)
# 读取对象属性
print(dog1.name)
# 调用方法
dog1.eat()