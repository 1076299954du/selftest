def fun(arg1, arg2):
    print('arg1', arg1, id(arg1))
    print('arg2', arg2, id(arg2))
    arg1 = 100
    arg2.append(10)
    print('arg1=', arg1, id(arg1))
    print('arg2=', arg2, id(arg2))


n1 = 11
n2 = [22, 33, 44]
print(n1, id(n1))
print(n2, id(n2))
print("--------")
fun(n1, n2)
print(n1, id(n1))
print(n2, id(n2))

