# 数组中的第K个最大元素
# 在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

# 示例 1:

# 输入: [3,2,1,5,6,4] 和 k = 2
# 输出: 5
# 示例 2:

# 输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
# 输出: 4
# 说明:

# 你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。

class Solution:
    def findKthLargest(self, nums: [int], k: int) -> int:
        k_arr = []
        for num in nums:
            if not k_arr:
                k_arr.append(num)
            else:
                # print(k_arr)
                insert_index = -1
                for (index, ka) in enumerate(k_arr):
                    if ka <= num:
                        insert_index = index
                        break
                if insert_index >= 0:
                    k_arr.insert(insert_index, num)
                else:
                    k_arr.append(num)
                if len(k_arr) > k:
                    k_arr.pop()
        return k_arr.pop()


print(Solution().findKthLargest([3,2,3,1,2,4,5,5,6], k = 4))
