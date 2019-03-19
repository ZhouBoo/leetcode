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
        # 23：60 23：（12345）（0~9）

        A.sort()
        max_hour = -1
        max_min = -1

        for h in A:
            list_A = A.copy()
            list_A.remove(h)
            for m in list_A:
                hour_one = h * 10 + m
                hour_one = -1 if hour_one > 23 else hour_one
                hour_two = m * 10 + h
                hour_two = -1 if hour_two > 23 else hour_two
                real_hour = max(hour_one, hour_two)
                if real_hour == -1:
                    continue

                new_A = A.copy()
                new_A.remove(m)
                new_A.remove(h)

                min_one = new_A[0] * 10 + new_A[1]
                min_one = -1 if min_one > 59 else min_one
                min_two = new_A[1] * 10 + new_A[0] 
                min_two = -1 if min_two > 59 else min_two
                real_min = max(min_one, min_two)
                # print('{}, {}'.format(real_hour, real_min))

                if real_min == -1:
                    continue

                if self.compare_time(max_hour, max_min, real_hour, real_min):
                    max_hour = real_hour
                    max_min = real_min

        if max_hour == -1 or max_min == -1:
            return ''
        return '{:0>2}:{:0>2}'.format(max_hour, max_min)

    def check_time(self, hour, min): 
        if hour <= 23 and min <= 59:
            return True
        return False

    def compare_time(self, hour, min, cp_hour, cp_min):
        if cp_hour > hour:
           return True
        elif hour == cp_hour and cp_min > min: 
            return True

        return False

print(Solution().largestTimeFromDigits([0,8,7,3]))
print(Solution().largestTimeFromDigits([1,2,3,4]))
print(Solution().largestTimeFromDigits([5,9,2,3]))
print(Solution().largestTimeFromDigits([0,0,0,0]))
print(Solution().largestTimeFromDigits([1,9,6,0]))
