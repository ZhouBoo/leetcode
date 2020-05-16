# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

# 示例 1:

# 输入: "abcabcbb"
# 输出: 3 
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

class Solution:
    def lengthOfLongestSubstring(self, s: str):
        max_length_str = ''
        temp_max_length = 0
        for c in s:
            if c not in max_length_str:
                max_length_str += c
            else:
                temp_max_length = max(len(max_length_str), temp_max_length)
                index = max_length_str.index(c)
                if index < len(max_length_str):
                    max_length_str = max_length_str[index + 1:]
                else:
                    max_length_str = ''
                max_length_str += c


        temp_max_length = max(len(max_length_str), temp_max_length)
        return temp_max_length


print(Solution().lengthOfLongestSubstring('abcabcbb'))
print(Solution().lengthOfLongestSubstring('bbbb'))
print(Solution().lengthOfLongestSubstring('pwwkew'))
print(Solution().lengthOfLongestSubstring(' '))
print(Solution().lengthOfLongestSubstring('aa'))
print(Solution().lengthOfLongestSubstring('aab'))