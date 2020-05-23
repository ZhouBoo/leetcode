# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。

# ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

# 搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

# 你可以假设数组中不存在重复的元素。

# 你的算法时间复杂度必须是 O(log n) 级别。

# 示例 1:

# 输入: nums = [4,5,6,7,0,1,2], target = 0
# 输出: 4
# 示例 2:

# 输入: nums = [4,5,6,7,0,1,2], target = 3
# 输出: -1


class Solution:
    def search(self, nums: [int], target: int) -> int:
        return self.mid_search(nums, 0, len(nums) - 1, target)
    
    def mid_search(self, nums, start, end, target):
        if start > end: return -1
        mid = int((end - start) * 0.5) + start
        # print('mid', mid)
        if nums[mid] == target:
            return mid
        elif nums[0] <= nums[mid]:
            if nums[0] <= target < nums[mid]:
                return self.mid_search(nums, start, mid-1, target)
                # print('right - reversed', mid+1, end)
            else:
                return self.mid_search(nums, mid+1, end, target)
                # print('left', start, mid-1)
        else:
            if nums[mid] < target <= nums[len(nums) - 1]:
                return  self.mid_search(nums, mid+1, end, target)
                # print('left - reversed', start, mid-1)
            else:
                return self.mid_search(nums, start, mid-1, target)
                # print('left', mid+1, end)
                

print(Solution().search([4,5,6,7,0,1,2], 0) == 4)
print(Solution().search([4,5,6,7,0,1,2], target = 3) == -1)
print(Solution().search([4,5,6,7,8,1,2,3], 8) == 4)
print(Solution().search([5,1,2,3,4], 1) == 1)
print(Solution().search([1], 0) == -1)
print(Solution().search([0], 0) == 0)
print(Solution().search([1,3,5],1) == 0)

# ------

    # def real_mid_search_enter(self, nums, target):
    #     return self.real_mid_search(nums, 0, len(nums) - 1, target)
    # def real_mid_search(self, nums, start, end, target):
    #     if start > end: return -1
    #     mid = int((end - start) * 0.5) + start
    #     if nums[mid] == target:
    #         return mid
    #     elif target < nums[mid]:
    #         return self.real_mid_search(nums, start, mid - 1, target)
    #     else:
    #         return self.real_mid_search(nums, mid+1, end, target)



# print(Solution().real_mid_search_enter([0,1,2,4,5,6,7], 1) == 1)
# print(Solution().real_mid_search_enter([0,1,2,4,5,6], 0) == 0)
# print(Solution().real_mid_search_enter([0,1,2,4,5,6], 4) == 3)
# print(Solution().real_mid_search_enter([0], 0) == 0)
# print(Solution().real_mid_search_enter([0], 4) == -1)

