'''
Author: duzerui
Date: 2026-11-27 15:23:26
LastEditors: duzerui
LastEditTime: 2026-11-27 17:02:50
Description: sys.argv :接收你在运行 python 脚本时，在命令行后面跟上的参数
'''
import sys

print("sys.argv 的全部内容：", sys.argv)
print("一共有多少项：", len(sys.argv))
print("第0项（脚本名）：", sys.argv[0])

if len(sys.argv) >= 2:
    print("第1个参数：", sys.argv[1])
if len(sys.argv) >= 3:
    print("第2个参数：", sys.argv[2])
    
