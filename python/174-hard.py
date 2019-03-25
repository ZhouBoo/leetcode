# 一些恶魔抓住了公主（P）并将她关在了地下城的右下角。地下城是由 M x N 个房间组成的二维网格。我们英勇的骑士（K）最初被安置在左上角的房间里，他必须穿过地下城并通过对抗恶魔来拯救公主。
# 骑士的初始健康点数为一个正整数。如果他的健康点数在某一时刻降至 0 或以下，他会立即死亡。
# 有些房间由恶魔守卫，因此骑士在进入这些房间时会失去健康点数（若房间里的值为负整数，则表示骑士将损失健康点数）
# 其他房间要么是空的（房间里的值为 0），要么包含增加骑士健康点数的魔法球（若房间里的值为正整数，则表示骑士将增加健康点数）。
# 为了尽快到达公主，骑士决定每次只向右或向下移动一步。

class Solution:
    def calculateMinimumHP(self, dungeon) -> int:
        len_row = len(dungeon)
        len_col = len(dungeon[0])

        dp = [[0 for i in range(len_col)] for i in range(len_row)]

        # print(dp[len_row - 1][len_col - 1])
        dp[len_row - 1][len_col - 1] = max(1, 1 - dungeon[len_row - 1][len_col - 1])
        
        for r in range(len_row - 2, -1, -1):
            dp[r][len_col - 1] = max(1, dp[r + 1][len_col - 1] - dungeon[r][len_col - 1])
        
        for c in range(len_col - 2, -1, -1):
            dp[len_row - 1][c] = max(1, dp[len_row - 1][c + 1] - dungeon[len_row - 1][c])

        for r in range(len_row - 2, -1, -1):
            for c in range(len_col - 2, -1, -1):
                dp[r][c] = max(1, min(dp[r + 1][c], dp[r][c + 1]) - dungeon[r][c])
        print(dp)
        return dp[0][0]
        
print(Solution().calculateMinimumHP([[-2,-3,3],[-5,-10,1],[10,30,-5]]))
# print(Solution().calculateMinimumHP([[0, 0]]))