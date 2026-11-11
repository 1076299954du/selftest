# 输出1到50之间所有的5的倍数
for item in range(1, 51):
    if item % 5 != 0:
        continue
    print(item)
while True:
    world = input('请输入单词：')
    if not world: break
    print('单词是：', world)


