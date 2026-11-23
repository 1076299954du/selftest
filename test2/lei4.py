#
# @Author: duzerui
# @Date: 2026-11-23 11:21:07
# @LastEditors: duzerui
# @LastEditTime: 2026-11-23 11:51:49
# @FilePath: \selftest\test2\lei4.py
# @Description: 文件功能描述
#
class Filter:
    def __init__(self):
        self.blocked = []
        self.count= 0  # 父类新增：统计过滤次数
    
    def filter(self, sequence):
        self.count += 1
        return [x for x in sequence if x not in self.blocked]  

class SPAMFilter(Filter):    #    SPAMFilter是Filter的子类
    def __init__(self):
        super().__init__()  # 调用父类的构造函数 如果没有这句一旦以后给父类加别的初始化逻辑，子类就会漏掉.比如上方的count
        self.blocked = ['SPAM']

f = Filter()
s = SPAMFilter()
print(f.filter([1, 2, 3]))
print(s.filter(['SPAM', 'SPAM', 'eggs', 'bacon', 'SPAM']))
print(issubclass(SPAMFilter, Filter))  #  isinstance(s, SPAMFilter)  # 确定对象是否是特定类的实例
print(s.count
    )  # 统计过滤次数