# 给定一个字符串，逐个翻转字符串中的每个单词。

 

# 示例 1：

# 输入: "the sky is blue"
# 输出: "blue is sky the"
# 示例 2：

# 输入: "  hello world!  "
# 输出: "world! hello"
# 解释: 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
# 示例 3：

# 输入: "a good   example"
# 输出: "example good a"
# 解释: 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。

import functools

class Solution:
    def reverseWords(self, s: str) -> str:
        reversed_s = reversed([x for x in filter(lambda a: a != '', s.split(' '))])
        try:
            return functools.reduce(lambda a, b: "%s %s" % (a, b), reversed_s)
        except TypeError:
            return ''
        
    

print(Solution().reverseWords("a good   example"))
print(Solution().reverseWords("  hello world!  "))
print(Solution().reverseWords("the sky is blue"))
print(Solution().reverseWords(""))
print(Solution().reverseWords(" "))

# a = 'a good   example'.split(' ')
# b = '  hello world!  '.split(' ')
# print(b)

# a = [1, 2, 3,4]
# print(list(filter(lambda a: a > 2, a)))