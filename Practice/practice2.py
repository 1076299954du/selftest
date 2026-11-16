# # 斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、
# 34、……。
# 在数学上，费波那契数列是以递归的方法来定义：
# F0 = 0 (n=0)
# F1 = 1 (n=1)
# Fn = F[n-1]+ F[n-2](n=>2)

# def fib(n):
#     a, b = 1, 1
#     for i in range(n - 1):
#         a = b
#         b = a + b
#         print(a, b)
#
#     return a

# print(fib(9))
# 打印9*9乘法表
for i in range(1, 10):
    for j in range(1, i+1):
       print("%d*%d=%d" % (i, j, i * j), end='\t')
    #print(i, '*', j, '=', i * j, end='\t')
    print()





