'''
Author: duzerui
Date: 2026-11-27 16:02:59
LastEditors: duzerui
LastEditTime: 2026-11-27 17:08:22
Description: os 模块
'''

import os

if __name__ == '__main__':
    # 当前工作目录
    print("当前目录：", os.getcwd())

    # 拼接路径
    target_path = os.path.join("test_dir", "hello.txt") # 作用：安全拼接文件路径，自动适配不同系统的路径分隔符
    print("拼接后的路径：", target_path)
    target_path1 = os.path.join("test_dir")

    # 判断文件夹是否存在，不存在就创建
    if not os.path.exists("test_dir"):
        os.mkdir("test_dir")
        print("文件夹创建成功")

    # 列出当前目录内容
    print("当前目录内容：", os.listdir("."))

    # 判断是否是文件
    
    print("是否是文件：", os.path.isfile(target_path))
    print("是否是文件夹：", os.path.isdir(target_path1))

