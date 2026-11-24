'''
Author: 杜泽瑞
Email: 1076299954@qq.com
Date: 2026-11-24 12:47:02
Description:构造方法  使用super函数。调用父类的构造函数
'''
#
# @Author: duzerui
# @Date: 2026-11-16 11:22:52
# LastEditors: Please set LastEditors
# LastEditTime: 2026-11-24 13:23:42
# @Description: 构造方法  使用super函数。调用父类的构造函数

class FooBar:
    def __init__(self, value=42):
        self.somevar = value

f = FooBar("This is a constructor argument")
print(f.somevar)


class Bird:
    def __init__(self):
        self.hungry = True

    def eat(self):
        if self.hungry:
            print('Aaaah ...')
            self.hungry = False
        else:
            print('No, thanks!')


class SongBird(Bird):
    def __init__(self):
        super().__init__()
        self.sound = "Squawk!"

    def sing(self):
        print(self.sound)


# b = Bird()
# b.eat()


sb = SongBird()
sb.sing()
sb.eat()
# print(sb.eat())


class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0
    def set_size(self,size):
        self.width,self.height = size
    def get_size(self):
        return self.width,self.height
r = Rectangle()
print(r.height)
print(r.width)
print("ssssss",r.get_size())
print(r.set_size((150,100)))
print(r.width)
print(r.get_size())

