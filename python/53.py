
# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

# 示例:

# 输入: [-2,1,-3,4,-1,2,1,-5,4],
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
# 进阶:

# 如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tp_sum = 0
        current_max = []
        temp_max = []

        for idx in range(0, len(nums)):
            num = nums[idx]
            if not temp_max:
                temp_max.append(num)
                tp_sum += num
            else:
                if tp_sum > tp_sum + num:
                    print("clear -> %s" % temp_max)
                    if not current_max or sum(current_max) < tp_sum:
                        current_max.clear()
                        current_max.extend(temp_max)
                    temp_max.clear()
                    temp_max.append(num)
                    tp_sum = num 
                else:
                    temp_max.append(num)
                    tp_sum += num

        return current_max

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(Solution().maxSubArray(nums))