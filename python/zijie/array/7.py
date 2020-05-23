# 第k个排列
# 给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。

# 按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：

# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# 给定 n 和 k，返回第 k 个排列。

# 说明：

# 给定 n 的范围是 [1, 9]。
# 给定 k 的范围是[1,  n!]。
# 示例 1:

# 输入: n = 3, k = 3
# 输出: "213"
# 示例 2:

# 输入: n = 4, k = 9
# 输出: "2314"

import math

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        every_batch = 1
        times = 1
        number_list = [x for x in range(1, n+1)]
        while n - 1 >= times:
            every_batch *= times
            times += 1
        # how many
        times -= 1
        nums = []
        # print('every_batch:', every_batch)
        while every_batch > 0 and len(number_list) > 1 and k > 0:
            index = math.ceil(k / every_batch) - 1
            # print("index:", index, k)
            if index < 0:
                break
            first_num = number_list[index]
            # print("first_num:", first_num, '|every_batch:', every_batch, '|times:',times, '|k:', k)
            # 这里去的不是具体 1234 的数字，而是取得当前是否调整过，例如 1234 ，第一位选1的时候不需要跳转，那么跳过的数目k也不需要调整
            k -= every_batch * (index)
            nums.append(first_num)
            number_list.remove(first_num)
            every_batch = every_batch // times
            times -= 1
        
        while len(number_list) > 0:
            nums.append(number_list[0])
            number_list.remove(number_list[0])
        r = ''
        for n in nums:
            r += '%d' % n
        return r

print(Solution().getPermutation(4, 9))
print(Solution().getPermutation(3, 3))
print(Solution().getPermutation(3, 1))
print(Solution().getPermutation(3, 5))
print(Solution().getPermutation(4, 2))

# print(math.ceil(2.5))