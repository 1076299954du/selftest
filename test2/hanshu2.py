def fun(num):
    odd = []
    even = []
    for i in num:
        if i % 2 == 0:
            odd.append(i)
        else:
            even.append(i)
    return odd, even


lst = [10, 29, 34, 23, 44, 53, 55]
print(fun(lst))


def fun1():
    print('hello')


fun1()
