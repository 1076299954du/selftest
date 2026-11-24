#
# @Author: 杜泽瑞
# @Email: 1076299954@qq.com
# @Date: 2026-11-16 11:22:52
# @LastEditors: duzerui
# @LastEditTime: 2026-11-24 17:38:51
# @Description: 文件功能描述
#
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return '我的名字是{0},今年{1}岁'.format(self.name, self.age)


stu = Student('张三', 20)
print(dir(stu))
print(stu)
print(type(stu))
