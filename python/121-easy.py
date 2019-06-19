# 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
# 如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。
# 注意你不能在买入股票前卖出股票。

class Solution:
    def maxProfit(self, prices: list) -> int:
        max_in = 0
        direction = None
        change_point = None
        for (idx, p) in enumerate(prices):
            if change_point is None:
                change_point = p
                continue
            if direction is None:
                direction = 1 if p > prices[idx - 1] else -1
                if direction == 1:
                    max_in = p - prices[idx - 1]

            cur_direction = 1 if p > prices[idx - 1] else -1
            if cur_direction != direction \
                and direction == -1:
                cur_p = prices[idx - 1]
                # 找更低的点
                change_point = change_point if change_point < cur_p else cur_p
            if cur_direction == 1:
                cur_m = p - change_point
                # print('cur_m = %d, cur_p = %d, change_p = %d' % (cur_m, p, change_point))
                max_in = max(cur_m, max_in)
            direction = cur_direction
        return max_in


print(Solution().maxProfit([7,1,5,3,6,4]))
print(Solution().maxProfit([7,1,5]))
print(Solution().maxProfit([1,5]))
print(Solution().maxProfit([1]))
print(Solution().maxProfit([2,1,2,1,0,1,2]))
                    

