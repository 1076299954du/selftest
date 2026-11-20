#
# @Author: duzerui
# @Date: 2026-11-20 14:24:45
# @LastEditors: duzerui
# @LastEditTime: 2026-11-20 18:17:32
# @FilePath: \selftest\test2\lei3.py
# @Description: 文件功能描述
#
'''
Author: 杜泽瑞
Email: 1076299954@qq.com
Date: 2026-11-20 13:21:50
Description: 动物体系（封装 + 继承 + 多态全部包含）
'''
# 父类：Animal（动物）
class Animal:
    def __init__(self, name, age=1):
        # 实例属性：封装，每个动物自己的名字
        self.name = name
        self.age = age
    # 对外提供读取私有数据的方法
    def get_age(self):
        return self.age
    # 父类预留方法，约定接口（用来实现多态）
    def speak(self):
        pass

    # 公共方法：所有动物都要吃东西，复用（继承）
    def eat(self):
        print(f"{self.name} 在吃东西")

    def __str__(self):
        return f"Animal(name={self.name}, age={self.__age})"


# 子类 Dog，继承 Animal
class Dog(Animal):
    def speak(self):
        # 重写speak方法
        print(f"{self.name}：汪汪汪！今年{self.get_age()}岁")


# 子类 Cat，继承 Animal
class Cat(Animal):
    def speak(self):
        print(f"{self.name}：喵喵喵！")


# 子类 Duck，继承 Animal
class Duck(Animal):
    def speak(self):
        print(f"{self.name}：嘎嘎嘎！")

# 子类 Duck，继承 Animal
class Bird(Animal):
    def speak(self):
        print(f"{self.name}：叽叽叽！")


# ✅ 多态核心函数：只要求传入的对象有 speak()
def let_animal_speak(animal: Animal):
    animal.speak()
    animal.get_age()


# ========== 测试代码 ==========
dog = Dog("旺财", 3)
cat = Cat("咪咪", 2)
duck = Duck("小黄", 1)
bird = Bird("小鸟", 1   )

# 调用统一的函数，写法一模一样，行为不一样（多态）
let_animal_speak(dog)
let_animal_speak(cat)
let_animal_speak(duck)
let_animal_speak(bird)

# 继承来的eat方法
dog.eat()
cat.eat()
duck.eat()
