
# 在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

 

# 示例:

# 现有矩阵 matrix 如下：

# [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ]
# 给定 target = 5，返回 true。

# 给定 target = 20，返回 false。


class Solution:
    def findNumberIn2DArray(self, matrix: [[int]], target: int) -> bool:
        height = len(matrix)
        if height <= 0: return False
        width = len(matrix[0])
        y = 0
        x = width - 1
        while y < height and x >= 0:
            value = matrix[y][x]
            if value == target:
                return True
            elif value < target:
                y += 1
            else:
                x -= 1
        return False
a = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

print(Solution().findNumberIn2DArray(a, 5))
print(Solution().findNumberIn2DArray(a, 20))
