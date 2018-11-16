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
        length = len(nums)
        min_num = min(nums)
    
        # nums.sort()
        for index_x in range(length):
            if nums[index_x] + min_num > target:
                continue
            for index_y in range(index_x + 1, length):
                # if nums[index_y] > target:
                #     print('max index_x = %d, index_y = %d' % (index_x, index_y))
                #     continue
                sum = nums[index_x] + nums[index_y]
                if sum == target:
                    print('sum = %d, x = %d, y = %d' % (sum, nums[index_x], nums[index_y]))
                    return [index_x, index_y]
        
        return [0, 0]

s = Solution()
# nums = [2, 7, 11, 15, 123, 4, 5,12, 20, 187, 10, 98]
# target = 108
nums = [-3,4,3,90]
target = 0
print(s.twoSum(nums, target))
