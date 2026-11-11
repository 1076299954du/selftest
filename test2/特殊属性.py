# 带参数时，返回参数的属性、方法列表
# print(dir(object))


class A:
    pass


class B:
    pass


class C(A, B):
    def __init__(self, name, age):
        self.name = name
        self.age = age


class D(A):
    pass


x = C('jack', 20)  # x是C类型的一个实例对象
print("========")
print(x.__dict__)  # 实例对象的属性字典
print(C.__dict__)
print('------')
print(x.__class__)  # 输出对象所处的类
print(C.__bases__)  # C类的父类类型的元素，类的基本元组（多继承）
print(C.__base__)  # 类的基类
print("********")
print(C.__mro__)  # 类的层次结构
print(A.__subclasses__())  # 子类列表


