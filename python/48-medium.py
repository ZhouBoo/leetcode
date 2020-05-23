# 给定一个 n × n 的二维矩阵表示一个图像。
# 将图像顺时针旋转 90 度。
# 说明：
# 你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。

# 旋转的借鉴思路
# 00 03
# 01 13
# 02 23
# 03 33

# 00 33
# 01 32
# 02 31
# 03 30

# 00 30
# 01 20
# 02 10
# 03 00


class Solution:
    def rotate(self, matrix: [[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # edge start
        edge_s = 0
        # edge end
        edge_e = len(matrix[0]) - 1
        if edge_e == edge_s:
            return
        level = 0
        # 每次移动的矩阵大框架的起始位置和末尾位置，一个一个的矩形往内压缩
        while edge_s < edge_e:
            # do trans 3 times for 4 side
            times = 3
            while times > 0:
                for point in range(edge_s, edge_e):
                    if times == 3:
                        obj_index_x = edge_e
                        obj_index_y = point
                    elif times == 2:
                        obj_index_x = edge_e - point + level
                        obj_index_y = edge_e
                    else:
                        obj_index_x = edge_s
                        obj_index_y = edge_e - point + level
                    # print('edge_s = %d edge_e = %d, [%d][%d] <=> target [%d][%d]' %
                    #       (edge_s, edge_e, level, point, obj_index_y, obj_index_x))
                    temp_number = matrix[level][point]
                    matrix[level][point] = matrix[obj_index_y][obj_index_x]
                    matrix[obj_index_y][obj_index_x] = temp_number
                # print(matrix)
                # print('----')
                times -= 1

            # update condition
            edge_s += 1
            edge_e -= 1
            level += 1


if __name__ == "__main__":
    s = Solution()

    matrix = [
        [1]
    ]
    s.rotate(matrix)
    print(matrix == [[1]])

    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    s.rotate(matrix)
    print(matrix == [[7, 4, 1], [8, 5, 2], [9, 6, 3]])

    matrix = [
        [1, 2],
        [4, 5]
    ]
    s.rotate(matrix)
    print(matrix == [[4, 1], [5, 2]])

    matrix = [
        [5, 1, 9, 11, 14],
        [2, 4, 8, 10, 51],
        [13, 3, 6, 7, 35],
        [15, 14, 12, 6, 76],
        [25, 4, 17, 56, 7]
    ]
    s.rotate(matrix)
    print(matrix == [[25, 15, 13, 2, 5], [4, 14, 3, 4, 1], [17, 12, 6, 8, 9], [56, 6, 7, 10, 11], [7, 76, 35, 51, 14]])

    matrix = [
        [5, 1, 9, 11],
        [2, 4, 8, 10],
        [13, 3, 6, 7],
        [15, 14, 12, 16]
    ]
    s.rotate(matrix)
    print(matrix == [[15,13, 2, 5],[14, 3, 4, 1],[12, 6, 8, 9],[16, 7,10,11]])

    