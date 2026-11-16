# 利用wile和break实现输入密码3次
a = 0
while a < 3:
    pwd = input('输入密码')
    if pwd == '8888':
        print('输入密码正确')
        break
    else:
        print('密码输入错误')
    a += 1
else:
    print("以上3次密码输入君错误")

