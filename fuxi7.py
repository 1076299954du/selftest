def in_the_middle(title, **params):  # 使用两个星号收集关键字参数，得到一个字典
    print(title)
    print(params)


in_the_middle('params:', something=42)  # params:   {'something': 42}


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