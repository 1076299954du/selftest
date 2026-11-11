# 统计文本文件中词语次数
from collections import defaultdict
import re


def count_words_in_file(file_path):
    with open(file_path,'r',encoding='utf-8') as file:

        text = file.read()


    #  使用正则表达式分割单词
    words = re.findall(r'\b\w+\b', text)

    # 统计单词出现次数
    words_counts = {}
    for word in words:
        if word in words_counts:
            words_counts[word]+=1
        else:
            words_counts[word]=1
    return words_counts

# 替换自己的文件路径

file_path ='test.txt'
word_counts = count_words_in_file(file_path)
print(word_counts)