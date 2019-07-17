# 给定一个无序的整数数组，找到其中最长上升子序列的长度。

# 示例:

# 输入: [10,9,2,5,3,7,101,18]
# 输出: 4 
# 解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
# 说明:

# 可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
# 你算法的时间复杂度应该为 O(n2) 。
# 进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?

class Solution:
    def lengthOfLIS(self, nums) -> int:
        lis = []
        for n in nums:
            self._put2mid(lis, n)
        return len(lis)

    def _put2mid(self, nums, target):
        last = len(nums) - 1
        if last < 0 or nums[last] < target:
            nums.append(target)
        elif nums[0] > target:
            nums[0] = target
        else:
            mid = 0
            _left, _right = 0, last
            while _left < _right:
                mid = int((_right - _left) / 2) + _left
                if nums[mid] > target:
                    _left, _right = 0, mid
                elif nums[mid] < target:
                    _left, _right = mid + 1, _right    
                else:
                    return
            if mid < len(nums) - 1:
                nums[mid + 1] = target

            




print(Solution().lengthOfLIS([2]) == 1)
print(Solution().lengthOfLIS([2, 2]) == 1)
print(Solution().lengthOfLIS([1, 2]) == 2)
print(Solution().lengthOfLIS([1, 2, 3, 6]) == 4)
print(Solution().lengthOfLIS([2, 8, 9, 1, 3, 4, 5]) == 4)
# print(Solution().lengthOfLIS([10,9,2,5,3,7,101,18]) == 4)
# print(Solution().lengthOfLIS([1,7,3,5,9,4,8]) == 4)

                


            
            

