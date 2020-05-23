# 最长连续序列
# 给定一个未排序的整数数组，找出最长连续序列的长度。

# 要求算法的时间复杂度为 O(n)。

# 示例:

# 输入: [100, 4, 200, 1, 3, 2]
# 输出: 4
# 解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。

class Solution:
    def longestConsecutive(self, nums: [int]) -> int:
        num_set = set()
        max_length = 0
        for num in nums:
            num_set.add(num)
        # print('total set', num_set)
        for num in nums:
            if num in num_set:
                num_set.remove(num)
                count = self.count(num+1, num_set, 1, True)
                count += self.count(num-1, num_set, 0, False)
                max_length = max(count, max_length)
        return max_length

    def count(self, num, num_set, count, isadd):
        if num in num_set:
            num_set.remove(num)
            # print(num, count, num_set)
            return self.count(num + 1 if isadd else num - 1, num_set, count+1, isadd)
        else:
            return count

print(Solution().longestConsecutive([100, 4, 200, 1, 3, 2]))
print(Solution().longestConsecutive([1,2,0,1,3]))

# a = {1:1, 2:1}

# print(a[1], a[3])

