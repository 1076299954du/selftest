'''
Author: duzerui
Date: 2026-11-27 16:52:00
LastEditors: duzerui
LastEditTime: 2026-11-27 17:49:32
Description: fileinput 模块
函数 / 方法	作用
fileinput.input(files=None, inplace=False, backup='')	核心入口，返回可逐行迭代的对象
fileinput.filename()	获取当前正在读取的文件名
fileinput.lineno()	所有文件累计的总当前行号
fileinput.filelineno()	当前文件内部的行号
fileinput.isfirstline()	判断当前行是不是当前文件的第一行
fileinput.isstdin()	判断当前是否在读取标准输入
fileinput.nextfile()	手动关闭当前文件，跳到下一个文件
fileinput.close()	关闭所有打开的文件
'''
import fileinput
import os
from pathlib import Path

print(os.getcwd())
# a.txt / b.txt 与脚本同目录；用脚本所在目录拼绝对路径，
# 这样无论从哪个工作目录启动，都能正确找到文件。
BASE_DIR = Path(__file__).resolve().parent
FILES = [BASE_DIR / 'a.txt', BASE_DIR / 'b.txt']

# 同时处理 a.txt 和 b.txt；文件内容为 UTF-8，必须显式指定 encoding
with fileinput.input(files=FILES, encoding='utf-8') as f:
    for line in f:
        # 只去掉行尾换行，避免误删行尾空格
        name = Path(fileinput.filename()).name
        print(f"{name}:{fileinput.filelineno()} - {line.rstrip('\r\n')}")



