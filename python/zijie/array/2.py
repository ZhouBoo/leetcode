# 岛屿的最大面积
# 给定一个包含了一些 0 和 1 的非空二维数组 grid 。

# 一个 岛屿 是由一些相邻的 1 (代表土地) 构成的组合，这里的「相邻」要求两个 1 必须在水平或者竖直方向上相邻。你可以假设 grid 的四个边缘都被 0（代表水）包围着。

# 找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为 0 。)


# 示例 1:

# [[0,0,1,0,0,0,0,1,0,0,0,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,1,1,0,1,0,0,0,0,0,0,0,0],
#  [0,1,0,0,1,1,0,0,1,0,1,0,0],
#  [0,1,0,0,1,1,0,0,1,1,1,0,0],
#  [0,0,0,0,0,0,0,0,0,0,1,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,0,0,0,0,0,0,1,1,0,0,0,0]]
# 对于上面这个给定矩阵应返回 6。注意答案不应该是 11 ，因为岛屿只能包含水平或垂直的四个方向的 1 。

# 示例 2:

# [[0,0,0,0,0,0,0,0]]
# 对于上面这个给定的矩阵, 返回 0。


# 注意: 给定的矩阵grid 的长度和宽度都不超过 50。


class Solution:

    def maxAreaOfIsland(self, grid: [[int]]) -> int:
        global width
        global height
        width = 0
        height = 0
        self.width = len(grid[0])
        self.height = len(grid)

        max_island = 0
        for (index_y, row) in enumerate(grid):
            for (index_x, point) in enumerate(row):
                max_island = max(max_island, self.land(grid, index_x, index_y, 0))
        return max_island

    def land(self, grid, x, y, count):
        # print(a)
        c = count
        if grid[y][x] == 1:
            # print(y, x)
            c += 1
            grid[y][x] = 0
        else:
            return c

        if x > 0:
            c = self.land(grid, x - 1, y, c)
        if x < self.width - 1:
            c = self.land(grid, x + 1, y, c)
        if y > 0:
            c = self.land(grid, x, y - 1, c)
        if y < self.height - 1:
            c = self.land(grid, x, y + 1, c)
        return c


b = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
     [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
     [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]

a = [
    [0, 0, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 0]
]

print(Solution().maxAreaOfIsland(a))
print(Solution().maxAreaOfIsland(b))
