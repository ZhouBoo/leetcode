# 如果一个由 '0' 和 '1' 组成的字符串，是以一些 '0'（可能没有 '0'）后面跟着一些 '1'（也可能没有 '1'）的形式组成的，
# 那么该字符串是单调递增的。
# 我们给出一个由字符 '0' 和 '1' 组成的字符串 S，我们可以将任何 '0' 翻转为 '1' 或者将 '1' 翻转为 '0'。
# 返回使 S 单调递增的最小翻转次数。

class Solution:
    def minFlipsMonoIncr(self, S):
        """
        :type S: str
        :rtype: int
        """

        # 左边的 1 有多少
        left_count = 0
        # 右边的 0 有多少
        right_count = S.count('0')

        current_min = right_count

        for (idx, s) in enumerate(S):
            if s == '0':
                right_count -= 1
            else:
                left_count  += 1
            current_min = min(current_min, right_count + left_count)
                
        return current_min


print(Solution().minFlipsMonoIncr("010110") == 2)
print(Solution().minFlipsMonoIncr("00110") == 1)
print(Solution().minFlipsMonoIncr("0011000") == 2)
print(Solution().minFlipsMonoIncr("11111") == 0)
print(Solution().minFlipsMonoIncr("0101100011") == 3)
print(Solution().minFlipsMonoIncr("011110110111111") == 2)
print(Solution().minFlipsMonoIncr("10011111110010111011") == 5)
# +1 -2 +7 -2 +1 -1 +3 -1 +2
# 1  -1 +6 +4 +5 +4 +7 +6 +8
