'''
Author: 杜泽瑞
Email: 1076299954@qq.com
Date: 2026-11-16 12:17:14
Description: 
'''
# 流程控制语句break与continue在二重循环中的使用
for i in range(5):
    for j in range(1, 11):
        if j % 2 == 0:
            continue
        print(j, end='\t')
    print(i)
