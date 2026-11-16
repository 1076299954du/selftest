file = open('b.text', 'a')
# file.write('hello,world')
# print(file.readlines())
# print(file.read(2))
# print(file.readlines())
lst = ['java', 'python']
file.writelines(lst)
file.close()
