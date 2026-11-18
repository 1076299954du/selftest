#
# @Author: duzerui
# @Date: 2026-11-16 11:22:52
# @LastEditors: duzerui
# @LastEditTime: 2026-11-18 11:51:40
# @FilePath: \selftest\fuxi\fuxi7.py
'''@Description: - `*args`：收集位置参数，打包成元组 tuple 。`**kwargs`：收集关键字参数，打包成字典 dict'''
#
def in_the_middle(title, **params):  # 使用两个星号收集关键字参数，得到一个字典
    print(title)
    print(params)

def print_params_2(title, *params):
    print(title)
    print(params)

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