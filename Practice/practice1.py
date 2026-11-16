# 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？


num_list = [1, 2, 3, 4]
count = 0

for i in num_list:
    for j in num_list:
        if j == i:
            continue
        for k in num_list:
            if k == i or k == j:
                continue
            else:
                print(i, j, k)
                count += 1

print("共有%d个不同的三位数" % count)