# 字符串的排列
# 给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。

# 换句话说，第一个字符串的排列之一是第二个字符串的子串。

# 示例1:

# 输入: s1 = "ab" s2 = "eidbaooo"
# 输出: True
# 解释: s2 包含 s1 的排列之一 ("ba").


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        windows_len = len(s1)
        index = 0
        sorted_s1 = sorted(s1)
        while index + windows_len <= len(s2):
            sorted_windows_s2 = sorted(s2[index: windows_len + index])
            if sorted_s1 == sorted_windows_s2:
                return True
            index += 1
        return False


print(Solution().checkInclusion('ab', 'eidbaooo'))
print(Solution().checkInclusion(s1= "ab", s2 = "eidboaoo"))
print(Solution().checkInclusion(s1= "adc", s2 = "dcda"))