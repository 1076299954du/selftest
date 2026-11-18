'''
Author: 杜泽瑞
Email: 1076299954@qq.com
Date: 2026-11-16 12:17:14
Description: 全局变量与局部变量学习
'''
# num = input('输入数字')


def fibs(num):
    result = [0, 1]
    for i in range(num - 2):
        result.append(result[-2] + result[-1])
        print(result)
    return result
    # print(result)


fibs(15)

x = 8
def outer():
    x = 20         # outer的局部x
    def inner():
        x = 99     # inner自己的局部x，和外面两个x互不干扰
        print(x)   # ① 99
    inner()
    print(x)       # ② outer里的x → 20
outer()
print(x)           # ③ 最外面全局x → 8


a = 5
def f1():
    a = 20          # f1的局部a
    def f2():
        nonlocal a  # 找上一层f1里面的a
        a = 30
        print(a)    # ① 30
    f2()
    print(a)        # ② f1的a被修改成30，打印30
f1()
print(a)            # ③ 全局a不受影响，依旧5


num = 100
def A():
    num = 10
    def B():
        global num   # 这里的num是【全局的num=100】
        num += 1     # 等价 num = 100 + 1 = 101
        print(num)
    B()
    print(num)       # 这个是A自己的局部num，还是10
A()
print(num)           # 全局num已经变成101

