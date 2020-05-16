# 三数之和
# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。

# 注意：答案中不可以包含重复的三元组。

 
# 示例：

# 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

# 满足要求的三元组集合为：
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]

class Solution:
    def threeSum(self, nums: [int]):
        sorted_nums = sorted(nums)
        tail_pointer = len(nums) - 1
        result = []

        for (index, num) in enumerate(sorted_nums):
            header_pointer = index + 1
            tp = tail_pointer
            while header_pointer < tp:
                a = sorted_nums[header_pointer]
                b = sorted_nums[tail_pointer]
                if num + a == b:
                    result.append([num, a, b])

        return result

print(Solution.threeSum([-1, 0, 1, 2, -1, -4]))
                    

                

