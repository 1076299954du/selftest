class Cpu:
    pass


class Disk:
    pass


class Computer:
    def __init__(self, cpu, disk):
        self.cpu = cpu
        self.disk = disk


# 赋值操作
cpu1 = Cpu()
cpu2 = cpu1
print(id(cpu1))
print(id(cpu2))
# 类的浅拷贝
print('----------')
disk = Disk()
computer1 = Computer(cpu1, disk)
import copy

computer2 = copy.copy(computer1)
print(computer1, computer1.cpu, computer1.disk)
print(computer2, computer2.cpu, computer2.disk)
# 深拷贝
print('---------')
computer3 = copy.deepcopy(computer1)
print(computer1, computer1.cpu, computer1.disk)
print(computer3, computer3.cpu, computer3.disk)
