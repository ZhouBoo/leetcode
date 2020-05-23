# 最长连续递增序列
# 给定一个未经排序的整数数组，找到最长且连续的的递增序列。

# 示例 1:

# 输入: [1,3,5,4,7]
# 输出: 3
# 解释: 最长连续递增序列是 [1,3,5], 长度为3。
# 尽管 [1,3,5,7] 也是升序的子序列, 但它不是连续的，因为5和7在原数组里被4隔开。 
# 示例 2:

# 输入: [2,2,2,2,2]
# 输出: 1
# 解释: 最长连续递增序列是 [2], 长度为1。


class Solution:
    def findLengthOfLCIS(self, nums: [int]) -> int:
        temp_array = []
        hp = 0
        for num in nums:
            if not temp_array:
                temp_array.append(num) 
            elif num > temp_array[hp]:
                hp += 1
                if hp < len(temp_array):
                    temp_array[hp] = num
                else:
                    temp_array.append(num)
            else:
                hp = 0
                temp_array[0] = num
            print(temp_array)
        return len(temp_array)

print(Solution().findLengthOfLCIS([1,3,5,4,7]))
print(Solution().findLengthOfLCIS([2,2,2,2,2]))