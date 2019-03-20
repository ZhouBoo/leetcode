# 一些恶魔抓住了公主（P）并将她关在了地下城的右下角。地下城是由 M x N 个房间组成的二维网格。我们英勇的骑士（K）最初被安置在左上角的房间里，他必须穿过地下城并通过对抗恶魔来拯救公主。

# 骑士的初始健康点数为一个正整数。如果他的健康点数在某一时刻降至 0 或以下，他会立即死亡。

# 有些房间由恶魔守卫，因此骑士在进入这些房间时会失去健康点数（若房间里的值为负整数，则表示骑士将损失健康点数）；其他房间要么是空的（房间里的值为 0），要么包含增加骑士健康点数的魔法球（若房间里的值为正整数，则表示骑士将增加健康点数）。

# 为了尽快到达公主，骑士决定每次只向右或向下移动一步。

class Solution:
    def calculateMinimumHP(self, dungeon) -> int:
        # r = [[1 for i in range(len(dungeon[0]))] for j in range(len(dungeon))]
        # print(r)
        p_index_r = len(dungeon) - 1
        p_index_c = len(dungeon[0]) - 1

        min_life = 1

        while p_index_c != 0 and p_index_r != 0:
            if dungeon[p_index_r][p_index_c] < 0:
                min_life -= dungeon[p_index_r][p_index_c]

            # if p_index_r - 1 > 0
            d_index_r = p_index_r - 1 if p_index_r - 1 > 0 else p_index_r 
            d_index_c = p_index_c - 1 if p_index_c - 1 > 0 else p_index_c

            d_min_life_r = min_life
            d_min_life_c = min_life

            if dungeon[p_index_r][d_index_c] < 0:
                d_min_life_c -= dungeon[p_index_r][d_index_c]
            
            if dungeon[d_index_r][p_index_c] < 0:
                d_min_life_r -= dungeon[d_index_r][p_index_c]

            if d_min_life_c < d_min_life_r:
                p_index_c = d_index_c
                min_life = d_min_life_c
            else:
                p_index_r = d_index_r
                min_life = d_min_life_r
        
        return min_life


print(Solution().calculateMinimumHP([[-2,-3,3],[-5,-10,1],[10,30,-5]]))