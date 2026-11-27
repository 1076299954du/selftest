'''
Author: duzerui
Date: 2026-11-27 16:52:00
LastEditors: duzerui
LastEditTime: 2026-11-27 18:55:06
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
import sys
from pathlib import Path

print(os.getcwd())
print(os.listdir()) # 查看当前目录有哪些文件
# a.txt / b.txt 与脚本同目录；用脚本所在目录拼绝对路径，
# 这样无论从哪个工作目录启动，都能正确找到文件。
BASE_DIR = Path(__file__).resolve().parent
print(BASE_DIR)
FILES = [BASE_DIR / 'a.txt', BASE_DIR / 'b.txt']

# 同时处理 a.txt 和 b.txt；文件内容为 UTF-8，必须显式指定 encoding
with fileinput.input(files=FILES, encoding='utf-8') as f:
    for line in f:
        # 只去掉行尾换行，避免误删行尾空格
        name = Path(fileinput.filename()).name
        print(f"{name}:{fileinput.filelineno()} - {line.rstrip('\r\n')}")


# ---------- 原地修改（inplace）演示 ----------
# inplace=True 时 fileinput 会把 sys.stdout 重定向到当前处理的输入文件：
# 循环里写出的内容就是该文件的新内容，原文件会被覆盖。
# backup='.bak' 会先把原文件另存为 a.txt.bak / b.txt.bak，便于恢复。
# 注意：每次运行都会覆盖上一份 .bak，因此另存了 .orig 作为初始快照。
RUN_INPLACE = True
OLD_TEXT, NEW_TEXT = '中国', 'China'

if RUN_INPLACE:
    with fileinput.input(files=FILES, inplace=True, backup='.bak',
                         encoding='utf-8') as f:
        for line in f:
            # 用 sys.stdout.write 写回，保留原行的换行符；
            # 若用 print() 会额外补一个换行，末行也会被强行加上换行。
            sys.stdout.write(line.replace(OLD_TEXT, NEW_TEXT))
            # 进度提示绝不能用 print，否则会被写进文件，只能输出到 stderr
            if fileinput.isfirstline():
                print(f"[inplace] 正在处理 {Path(fileinput.filename()).name}",
                      file=sys.stderr)

    # 离开 with 后 sys.stdout 已恢复，可以正常打印到屏幕
    print("原地修改完成，备份文件为 *.bak")
    for path in FILES:
        print(f"--- {path.name} ---")
        print(path.read_text(encoding='utf-8'), end='')



