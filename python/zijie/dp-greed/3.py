# 最大正方形
# 在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。

# 示例:

# 输入:

# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0

# 输出: 4


class Solution:
    def maximalSquare(self, matrix: [[str]]) -> int:
        max_w = 0
        w = len(matrix)
        if w <= 0:
            return 0

        for (y, row) in enumerate(matrix):
            for (x, p) in enumerate(row):
                v = int(p)
                if v == 1 and max_w == 0:
                    max_w = 1
                if x == 0 or y == 0 or v == 0:
                    continue
                else:
                    min1 = min(int(matrix[y-1][x]), int(matrix[y-1][x-1]))
                    min1 = min(int(matrix[y][x-1]), min1)
                    matrix[y][x] = min1 + 1
                    max_w = max(max_w, min1 + 1)
        return max_w * max_w


a = [["1", "0", "1", "0", "0"],
     ["1", "0", "1", "1", "1"],
     ["1", "1", "1", "1", "1"],
     ["1", "0", "0", "1", "0"]]

b = [["1", "0", "1", "0", "0"],
     ["1", "0", "1", "1", "1"],
     ["1", "1", "1", "1", "1"],
     ["1", "0", "0", "1", "0"]]

b = [["1", "1"]]
# b = [[]]
print(Solution().maximalSquare(b))
print(Solution().maximalSquare(a))