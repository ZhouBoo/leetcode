# 最长公共前缀
# 编写一个函数来查找字符串数组中的最长公共前缀。

# 如果不存在公共前缀，返回空字符串 ""。
# 示例 1:

# 输入: ["flower","flow","flight"]
# 输出: "fl"


class Solution:
    def longestCommonPrefix(self, strs):
        index_pointer = 0
        common_prefix = ''
        while True:
            temp_prefix = None
            for str in strs:
                if len(str) <= index_pointer:
                    return common_prefix
                else:
                    if not temp_prefix:
                        temp_prefix = str[index_pointer]
                    elif temp_prefix != str[index_pointer]:
                            return common_prefix
            if not temp_prefix:
                return ''
            index_pointer += 1
            common_prefix += temp_prefix
        return common_prefix


print(Solution().longestCommonPrefix(["flower","flow","flight"]))
print(Solution().longestCommonPrefix(["dog","racecar","car"]))
print(Solution().longestCommonPrefix([]))