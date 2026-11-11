# 求素数


def is_prime(n):
    if num < 2:
        return False
    for i in range(2, int(num **0.5)+1):
        if num % i ==0:
            return False
    return True


count = 0
for num in range(100, 201):
    if is_prime(num):
        print(num)
        count=count+1
print("101-200之间共有", count, "个素数。")




