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