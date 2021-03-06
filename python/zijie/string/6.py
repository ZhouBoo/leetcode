# 简化路径
# 以 Unix 风格给出一个文件的绝对路径，你需要简化它。或者换句话说，将其转换为规范路径。

# 在 Unix 风格的文件系统中，一个点（.）表示当前目录本身；此外，两个点 （..） 表示将目录切换到上一级（指向父目录）；两者都可以是复杂相对路径的组成部分。更多信息请参阅：Linux / Unix中的绝对路径 vs 相对路径

# 请注意，返回的规范路径必须始终以斜杠 / 开头，并且两个目录名之间必须只有一个斜杠 /。最后一个目录名（如果存在）不能以 / 结尾。此外，规范路径必须是表示绝对路径的最短字符串。


# 示例 1：

# 输入："/home/"
# 输出："/home"
# 解释：注意，最后一个目录名后面没有斜杠。

import functools

class Solution:
    def simplifyPath(self, path: str) -> str:
        real_path_compents = []
        for location in path.split('/'):
            if not location or location == '.':
                continue
            if location == '..':
                if not real_path_compents:
                    continue
                real_path_compents.pop()
            else:
                real_path_compents.append(location)
        if real_path_compents:
            return '/' + functools.reduce(lambda a, b: a + '/' + b, real_path_compents)
        else:
            return '/'



a = '/a/../../b/../c//.//'
b = "/home//foo/"
c = "/a/../../b/../c//.//"
d = "/a//b////c/d//././/.."
e = "/../"
# print(Solution().simplifyPath(a))
# print(Solution().simplifyPath(b))
# print(Solution().simplifyPath(c))
# print(Solution().simplifyPath(d))
print(Solution().simplifyPath(e))
