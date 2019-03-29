# 一个N x N的网格(grid) 代表了一块樱桃地，每个格子由以下三种数字的一种来表示：

# 0 表示这个格子是空的，所以你可以穿过它。
# 1 表示这个格子里装着一个樱桃，你可以摘到樱桃然后穿过它。
# -1 表示这个格子里有荆棘，挡着你的路。
# 你的任务是在遵守下列规则的情况下，尽可能的摘到最多樱桃：

# 从位置 (0, 0) 出发，最后到达 (N-1, N-1) ，只能向下或向右走，并且只能穿越有效的格子（即只可以穿过值为0或者1的格子）；
# 当到达 (N-1, N-1) 后，你要继续走，直到返回到 (0, 0) ，只能向上或向左走，并且只能穿越有效的格子；
# 当你经过一个格子且这个格子包含一个樱桃时，你将摘到樱桃并且这个格子会变成空的（值变为0）；
# 如果在 (0, 0) 和 (N-1, N-1) 之间不存在一条可经过的路径，则没有任何一个樱桃能被摘到。

class Solution:
    def cherryPickup(self, grid) -> int:
        len_row = len(grid)
        len_col = len(grid[0])

        dp_go = [[0 for i in range(len_col)] for i in range(len_row)]

        dp_go[len_row - 1][len_col - 1] = grid[len_row - 1][len_col - 1]
        
        for r in range(len_row - 2, -1, -1):
            dp_go[r][len_col - 1] = dp_go[r + 1][len_col - 1] + grid[r][len_col - 1]

        for c in range(len_col - 2, -1, -1):   
            dp_go[len_row - 1][c] = dp_go[len_row - 1][c + 1] + grid[len_row - 1][c]

        for r in range(len_row - 2, -1, -1):
            for c in range(len_col - 2, -1, -1):
                if grid[r][c + 1] == -1 and grid[r + 1][c] == -1:
                    dp_go[r][c] = -1
                else:    
                    dp_go[r][c] = max(dp_go[r][c + 1] + grid[r][c], dp_go[r + 1][c] + grid[r][c])

        print('dp_go = ', dp_go)
        print('dp_max = ', dp_go[0][0])

        if dp_go[min(1, len_row - 1)][0] == -1 and dp_go[0][min(1, len_col - 1)] == -1:
            return 0

        dp_back_row, dp_back_col = 0, 0
        while dp_back_col < len_col and dp_back_row < len_row:
            grid[dp_back_row][dp_back_col] = 0
            if dp_back_col == len_col - 1:
                dp_back_row += 1
            elif dp_back_row == len_row - 1:
                dp_back_col += 1
            elif dp_go[dp_back_row + 1][dp_back_col] > grid[dp_back_row][dp_back_col + 1]:
                dp_back_row += 1
            else:
                dp_back_col += 1
        print('grid clean = ', grid)
        dp_back = [[0 for i in range(len_col)] for i in range(len_row)]
        dp_back[len_row - 1][len_col - 1] = grid[len_row - 1][len_col - 1]

        for r in range(len_row - 2, -1, -1):
            dp_back[r][len_col - 1] = dp_back[r + 1][len_col - 1] + grid[r][len_col - 1]
        
        for c in range(len_col - 2, -1, -1):
            dp_back[len_row - 1][c] = dp_back[len_row - 1][c + 1] + grid[len_row - 1][c]

        for r in range(len_row - 2, -1, -1):
            for c in range(len_col - 2, -1, -1):
                if grid[r][c + 1] == -1 and grid[r + 1][c] == -1:
                    dp_back[r][c] = -1
                else:
                    dp_back[r][c] = max(dp_back[r][c + 1] + grid[r][c], dp_back[r + 1][c] + grid[r][c])
        print('dp_back = ', dp_back)
        if dp_back[0][0] > 0:
            return dp_back[0][0] + dp_go[0][0]
        
        return dp_go[0][0]
      
# print(Solution().cherryPickup([[0,1,-1],[1,0,-1],[1,1,1]]) == 5)
# print(Solution().cherryPickup([[1,1,-1],[1,-1,1],[-1,1,1]]) == 0)
# print(Solution().cherryPickup([[0]]) == 0)
print(Solution().cherryPickup([[1,1,1,1,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,0,0,1],[1,0,0,1,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,1,1,1]]) == 15)
