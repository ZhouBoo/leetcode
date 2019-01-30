# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

# 你的算法时间复杂度必须是 O(log n) 级别。

# 如果数组中不存在目标值，返回 [-1, -1]。

class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = [-1, -1]
        start = 0
        end = len(nums) - 1

        while end >= start:
            mid_index = int((end + start) / 2)
            mid_value = nums[mid_index]
            if mid_value < target:
                print('mid_value < target')
                start = mid_index + 1
                print('end = %d, start = %d, mid = %d' % (end, start, mid_index))
            elif mid_value > target:
                print('mid_value %d > target %d' % (mid_value, target))
                end = mid_index - 1
                print('end = %d, start = %d, mid = %d' % (end, start, mid_index))
            else:
                print("found")
                result = [mid_index, mid_index]
                header_index = mid_index - 1
                tail_index = mid_index + 1
                while header_index >= 0 and nums[header_index] == mid_value:
                    result[0] = header_index
                    header_index -= 1
                    
                while tail_index < len(nums) and nums[tail_index] == mid_value:
                    result[1] = tail_index
                    tail_index += 1

                break

        return result

s = Solution()

nums = [5,7,7,8,8,10]
target = 6
# nums = [5,7,7,8,8,10]
# target = 8
# nums = [1]
# target = 1

# nums = [2, 2]
# target = 2

# nums = [5,7,7,8,8,10]
# target = 8

# nums = [1]
# target = 1
print(s.searchRange(nums, target))