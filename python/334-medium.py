# 给定一个未排序的数组，判断这个数组中是否存在长度为 3 的递增子序列。

# 数学表达式如下:

# 如果存在这样的 i, j, k,  且满足 0 ≤ i < j < k ≤ n-1，
# 使得 arr[i] < arr[j] < arr[k] ，返回 true ; 否则返回 false 。
# 说明: 要求算法的时间复杂度为 O(n)，空间复杂度为 O(1) 。

# 示例 1:

# 输入: [1,2,3,4,5]
# 输出: true

class Solution:
    def increasingTriplet(self, nums: [int]) -> bool:
        mins = []
        for n in nums:
            if len(mins) >= 3:
                break
            self._put2mid(mins, n)
        return len(mins) >= 3
            

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


print(Solution().increasingTriplet([1,2,3,4,5]) == True)
print(Solution().increasingTriplet([5,4,3,2,1]) == False)
print(Solution().increasingTriplet([1,4,2,5,0]) == True)
print(Solution().increasingTriplet([1,5,2,2,1]) == False)
print(Solution().increasingTriplet([2,1,5,0,4,6]) == True)