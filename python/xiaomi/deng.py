import re
#匹配以chinahadoop开头的字符串
result = re.match("chinahadoop","chinahadoop.cn")
#打印匹配出来的内容
print(result.group())

a = (1,2,3)
b = [7,8,9,0]
print(dict(zip(a,b))) 


a = [1, 9, 8, 3, 29]
b = [item / 2 if (index % 2 == 0) else item for index, item in enumerate(a)]

from random import randrange
b = randrange(1, 10, 3)
print(b)

# .	    匹配除“\n”之外的任意单个字符
# \d	匹配0到9之间的一个数字，等价于[0-9]
# \D	匹配一个非数字字符，等价于[^0-9]
# \s	匹配任意空白字符，如空格、制表符“\t”、换行“\n”等
# \S	匹配任意非空白字符
# \w	匹配任意单词字符（包含下划线），如a-z，A-Z，0-9，_等
# \W	匹配任意非单词字符，等价于[^ a-zA-Z0-9_]
# [ ]	匹配[ ]中列举的字符
# ^	    取反

from collections import Counter

c=Counter({'ham': 1, 'eggs': 2, 'apple': 1,'banana':-1})
# print(c)
b=Counter({'orange':0})
# print(b)
print (c-b)