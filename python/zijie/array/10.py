# 接雨水
# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

# 上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢 Marcos 贡献此图。
# 示例:


class Solution:
    def trap(self, height: [int]) -> int:
        if len(height) <= 0: return 0
        left = 0
        right = len(height) - 1
        left_higher = 0
        right_higher = 0
        weight = 0
        while left < right:
            if left_higher > height[left]:
                weight += left_higher - height[left]
            else:
                left_higher = height[left]

            if right_higher > height[right]:
                weight += right_higher - height[right]
            else:
                right_higher = height[right]

            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
                
        return weight



print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))