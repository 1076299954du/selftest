class Persion:
    def __new__(cls, *args, **kwargs):  # 用于创建对象
        print('__new__被调用，cls的ID值为{0}'.format(id(cls)))
        obj = super().__new__(cls)
        print('创建对象的ID为{0}'.format(id(obj)))
        return obj

    def __init__(self, name, age):  # 对创建的对象进行初始化
        print('__init__被调用,self的ID值为{0}'.format(id(self)),)
        self.name = name
        self.age = age


print('object这个类对象的id为{0}'.format(id(object)))
print('Persion这个类对象的id为{0}'.format(id(Persion)))
# 创建Persion类的实例对象
p1 = Persion('zhangsan', 55)
print('p1这个Persion类实例对象的ID：{0}'.format(id(p1)))
