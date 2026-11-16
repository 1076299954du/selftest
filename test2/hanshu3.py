try:
    def fun(a, b=10):
        print(a, b)


    fun(100)
    fun(20, 30)
except BaseException as e:
    pass
else:
    pass