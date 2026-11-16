# 键盘输入三次密码
for item in range(0, 3):
    pwd = input('输入密码')
    if pwd == '888':
        print('输入密码正确')
        break
    else:
        print('输入密码错误')
