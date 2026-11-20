'''
Author: 杜泽瑞
Email: 1076299954@qq.com
Date: 2026-11-16 12:17:14
Description: 多态的学习
'''
class Animal(object):
    def eat(self):
        print("动物会吃")


class Dog(Animal):
    def eat(self):
        print('狗吃热肉')


class Cat(Animal):
    def eat(self):
        print('猫吃鱼')


class Persion(object):
    def eat(self):
        print("人吃五谷杂粮")


# 定义一个函数
def fun(obj):
    obj.eat()


# 开始调用函数
fun(Cat())
fun(Dog())
fun(Animal())
fun(Persion())
 
class Dog:
    def speak(self):
        print("汪汪")

class Cat:
    def speak(self):
        print("喵喵")

class Duck:
    def speak(self):
        print("嘎嘎")

# ✅ 统一入口！这就是多态的核心
def let_it_speak(animal):
    # 固定写法：调用 .speak()
    animal.speak()


dog = Dog()  # 创造实例对象
cat = Cat()
duck = Duck()

# 调用形式完全一样！都是 let_it_speak(xxx)
let_it_speak(dog)   # 汪汪
let_it_speak(cat)   # 喵喵
let_it_speak(duck)  # 嘎嘎




