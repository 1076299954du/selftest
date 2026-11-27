'''
Author: duzerui
Date: 2026-11-16 11:22:52
LastEditors: duzerui
LastEditTime: 2026-11-27 17:05:06
Description: `__name__` 是每个 Python 文件（模块）自带的内置变量：
**用来标记：这个文件现在是【直接运行】，还是【被别的文件 import 导入】**
'''
def add(a, b):
    return a+b

import os
if __name__ == '__main__':
    # 这里面的代码，只有直接运行本文件才会执行
    # 如果被别人import导入，这一块代码不会跑
    print(add(10, 20))
  


