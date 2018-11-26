# 给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。
# 你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。

# 示例:

# 给定 nums = [2, 7, 11, 15], target = 9
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        current_sets = set()
        find_idx = None
        find_caculator = None
        for (idx, num) in enumerate(nums):
            caculator = target - num
            if num in current_sets:
                find_idx = idx
                find_caculator = caculator
                break
            else:
                print('current set: %s' % current_sets)
                current_sets.add(caculator)

        if find_idx:
            return [nums.index(find_caculator), find_idx]

s = Solution()
nums = [2, 7, 11, 15, 123, 4, 5,12, 20, 187, 10, 98]
target = 108
# nums = [-3,4,3,90]
# target = 0
print(s.twoSum(nums, target))
