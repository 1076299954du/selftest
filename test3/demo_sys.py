'''
Author: duzerui
Date: 2026-11-27 15:35:15
LastEditors: duzerui
LastEditTime: 2026-11-27 15:35:24
Description:  demo_sys.py
'''
# demo_sys.py
import sys

def main():
    # 1. 打印脚本传入的全部命令行参数
    print("=== sys.argv 命令行参数 ===")
    print(f"参数列表：{sys.argv}")
    print(f"脚本名 argv[0]：{sys.argv[0]}")

    # 判断是否传了参数
    if len(sys.argv) < 3:
        print("\n❌ 参数不足！使用方式：python demo_sys.py 数字1 数字2")
        sys.exit(1)  # 异常退出，返回码1

    # 拿到两个参数，转成数字
    num1 = float(sys.argv[1])
    num2 = float(sys.argv[2])
    print(f"\n✅ 拿到两个数字：{num1} , {num2}")
    print(f"相加结果：{num1 + num2}")

    # 2. 查看模块搜索路径（sys.path）
    print("\n=== sys.path 模块搜索路径（前3条）===")
    for p in sys.path[:3]:
        print(p)

    # 3. 查看当前Python版本和系统平台
    print("\n=== 环境信息 ===")
    print(f"Python版本: {sys.version}")
    print(f"运行平台: {sys.platform}")

    # 正常退出，返回码0
    sys.exit(0)


if __name__ == '__main__':
    main()
