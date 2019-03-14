# 949. 给定数字能组成的最大时间
# 给定一个由 4 位数字组成的数组，返回可以设置的符合 24 小时制的最大时间。
# 最小的 24 小时制时间是 00:00，而最大的是 23:59。从 00:00 （午夜）开始算起，过得越久，时间越大。
# 以长度为 5 的字符串返回答案。如果不能确定有效时间，则返回空字符串。

# 示例 1：
# 输入：[1,2,3,4]
# 输出："23:41"

# 示例 2：
# 输入：[5,5,5,5]
# 输出：""

class Solution:
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        # first_array = [0, 1, 2, 3]
        # second_array = [0, 1, 2, 3, 4]
        # third_array = [0, 1, 2, 3, 4, 5, 6]
        # fourth_array = [0, ]

        # 其中只能有一个超过6的数
        # 保证小时尽可能大
        # 23：60 23：（12345）（0~9）

        A.sort()
        if A[2] >= 6:
            return ''
        return '1'


print(Solution().largestTimeFromDigits([0,8,7,3]))
