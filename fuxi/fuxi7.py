'''
Author: duzerui
Date: 2026-11-16 11:22:52
LastEditors: duzerui
LastEditTime: 2026-11-24 18:01:03
@Description: - `*args`：收集位置参数，打包成元组 tuple 。`**kwargs`：收集关键字参数，打包成字典 dict。*（单独）分隔符，
不接受参数。后面的参数必须key=值'''

def in_the_middle(title, **params):  # 使用两个星号收集关键字参数，得到一个字典
    print(title)
    print(params)

def print_params_2(title, *params): # 使用一个星号收集参数，得到一个元组
    print('@@@@@',title)
    print('@@@@',params)

in_the_middle('params:', something=42)  # params:   {'something': 42}
print_params_2('params:',1,2,3)  

def in_the_middle1(title, *params):  # 使用一个星号收集参数，得到一个元组
    print(title)
    print(params)


in_the_middle1('params:', 42)  # params:  (42,)


def in_the_middle2(x, y, z=3, *title, **params, ):  # 两者结合使用
    print(x, y, z)
    print(title)
    print(params)


in_the_middle2(1, 2, 3, 4, 5, 6, 7, title=1, parmams=2)  # 1 2 3  (4, 5, 6, 7) {'title': 1, 'parmams': 2}
in_the_middle2(1, 2)  # 1 2 3 () {}


def hello(greeting='hello', name='world'):
    print('{},{}!'.format(greeting, name))


hello()
params = {'name': '哈哈哈', 'greeting': '99'}
hello(**params)


''' 单独 `*` 不叫 args，它是分界线：*后面的参数，必须用关键字传'''
def demo(x, *, y, z):
    print(x,y,z)

demo(10, y=20, z=30)  # ✅ 正确
# demo(10,20,30)        # ❌ 报错！y、z是仅限关键字参数
