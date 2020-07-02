# 请实现一个函数，把字符串 s 中的每个空格替换成"%20"。

#  

# 示例 1：

# 输入：s = "We are happy."
# 输出："We%20are%20happy."

import functools

class Solution:
    def replaceSpace(self, s: str) -> str:
        final_arr = []
        for char in s:
            if char == ' ':
                final_arr.extend(['%', '2', '0'])
            else:
                final_arr.append(char)
        return ''.join(final_arr)
            
print(Solution().replaceSpace( "We are happy."))

