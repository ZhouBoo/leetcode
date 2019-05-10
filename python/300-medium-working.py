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
    # def lengthOfLIS(self, nums) -> int:
    #     length = len(nums)
    #     for i in range(1, length):
    #         for h in range(i+1, length):
    #             if nums[h] > nums[i]:、
    #     stop_index = 0
    #     max_lengths = [1]
        
    #         if index == 0:
    #             continue
    #         else:
    #             if value > nums[index - 1]:
    #                 max_lengths.append(max_lengths[index - 1] + 1)
    #             else:
    #                 if value >= nums[stop_index]:
    #                     max_lengths.append(max_lengths[index - 1])
    #                 else:
    #                     max_lengths.append(1)
    #                     stop_index = index
    #     print(max_lengths)
    #     return max(max_lengths)


# print(Solution().lengthOfLIS([10,9,2,5,3,7,101,18]) == 4)
print(Solution().lengthOfLIS([1,7,3,5,9,4,8]) == 4)

                


            
            

