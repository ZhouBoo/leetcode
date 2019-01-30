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
        fix_string = '%d' % int(S)
        print('begin ===> %s\n' % fix_string)
        last_number = None
        last_count = None
        change_count = 0
        temp_count = 0
        change_count = 0
        length = len(fix_string)
        jump_next = False

        for (idx, s) in enumerate(fix_string):
            temp_count += 1
            if not last_count:
                last_count = 0

            if idx + 1 >= length or s != fix_string[idx + 1]:
                if not jump_next:
                    if last_count > temp_count:
                        print('++ current -- last count = %d, current count = %d' % (last_count, temp_count))
                        change_count += temp_count
                        jump_next = True

                    if temp_count > last_count:
                        print('++ last -- last count = %d, current count = %d' % (last_count, temp_count))
                        change_count += last_count

                else:
                    jump_next = False

                last_count = temp_count
                temp_count = 0
                last_number = s

        return change_count


print(Solution().minFlipsMonoIncr("010110") == 2)
print(Solution().minFlipsMonoIncr("00110") == 1)
print(Solution().minFlipsMonoIncr("0011000") == 2)
print(Solution().minFlipsMonoIncr("11111") == 0)
print(Solution().minFlipsMonoIncr("0101100011") == 3)
print(Solution().minFlipsMonoIncr("011110110111111") == 2)
print(Solution().minFlipsMonoIncr("10011111110010111011") == 5)
# +1 -2 +7 -2 +1 -1 +3 -1 +2
# 1  -1 +6 +4 +5 +4 +7 +6 +8