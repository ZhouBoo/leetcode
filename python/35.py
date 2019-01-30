# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

# 你可以假设数组中无重复元素。

class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        for idx, num in enumerate(nums):
            if num >= target:
                return idx
        idx = len(nums)
        return idx if idx >= 0 else 0


s = Solution()
x = s.searchInsert([1,3,5,6], 7)
print(x)