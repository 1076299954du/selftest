# num = input('输入数字')


def fibs(num):
    result = [0, 1]
    for i in range(num - 2):
        result.append(result[-2] + result[-1])
        print(result)
    return result
    # print(result)


fibs(15)
