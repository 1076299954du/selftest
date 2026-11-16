'''
Author: 杜泽瑞
Email: 1076299954@qq.com
Date: 2026-11-05 13:41:51
Description:   
'''
print("正在学习")
# name = input("输入姓名")
# print(name)
sentence = input("Sentence: ") 
screen_width = 80 
text_width = len(sentence) 
box_width = text_width + 6 
left_margin = (screen_width - box_width) // 2 
print() 
print(' ' * left_margin + '+' + '-' * (box_width-2) + '+') 
print(' ' * left_margin + '| ' + ' ' * text_width + ' |') 
print(' ' * left_margin + '| ' + sentence + ' |') 
print(' ' * left_margin + '| ' + ' ' * text_width + ' |') 
print(' ' * left_margin + '+' + '-' * (box_width-2) + '+')
print()