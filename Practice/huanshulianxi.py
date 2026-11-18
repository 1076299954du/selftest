'''
Author: 杜泽瑞
Email: 1076299954@qq.com
Date: 2026-11-18 09:26:46
Description: 
'''
def lookup(data, label, name):
    # 查找函数：如果 label 在data里，再找name对应的列表
    if label in data and name in data[label]:
        return data[label][name]
    return None

def store(data, full_name):
    names = full_name.split()
    # 目标：保证 names 长度固定为3（first, middle, last）
    if len(names) == 2:
        names.insert(1, '')
    # 如果是3个名字（Magnus Lie Hetland）刚好匹配
    labels = 'first', 'middle', 'last'
    for label, name in zip(labels, names):
        # 外层label不存在就先建空字典
        if label not in data:
            data[label] = {}
        people = lookup(data, label, name)
        if people:
            people.append(full_name)
        else:
            data[label][name] = [full_name]


MyNames = {}
store(MyNames, 'Magnus Lie Hetland')
store(MyNames, 'li ming')
print(MyNames)
