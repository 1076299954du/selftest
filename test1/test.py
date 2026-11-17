'''
Author: 杜泽瑞
Email: 1076299954@qq.com
Date: 2023-09-10 16:36:35
Description: 斐波那契数  下一项=前两项之和
'''
fibs = [0,1]
for i in range(8):
    next_fib = fibs[-2] + fibs[-1]
    fibs.append(next_fib)
print(fibs)

  