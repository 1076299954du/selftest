'''
Author: duzerui
Date: 2026-11-11 16:01:18
LastEditors: Please set LastEditors
LastEditTime: 2026-11-14 10:04:03
Description: 文件功能描述
'''
from math import e
print("dddd")
print(f"e的值是：{e}")
phonebook ={'bbb': '13812345678', 'aaa': '13812345555678', 'ccc': '13812345678'}
print(phonebook)
print('dddddde 的电话是{aaa}'.format_map(phonebook))
name = 'aaa'
salutation = 'bbb'
greeting = 'dddd'
print(name, salutation, greeting)
print(name,',', salutation, greeting)
print(name+',', salutation, greeting)