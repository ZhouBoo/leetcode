# 有一些工作：difficulty[i] 表示第i个工作的难度，profit[i]表示第i个工作的收益。

# 现在我们有一些工人。worker[i]是第i个工人的能力，即该工人只能完成难度小于等于worker[i]的工作。

# 每一个工人都最多只能安排一个工作，但是一个工作可以完成多次。

# 举个例子，如果3个工人都尝试完成一份报酬为1的同样工作，那么总收益为 $3。如果一个工人不能完成任何工作，他的收益为 $0 。

# 我们能得到的最大收益是多少？

class Solution:
    def maxProfitAssignment(self, difficulty, profit, worker):
        current_diff_index = 0
        max_profit_index = -1
        max_profit_sum = 0
        dp = zip(difficulty, profit)
        from operator import itemgetter
        dp = list(dp)
        dp.sort(key=itemgetter(0))
        print(dp)
        worker.sort()
        print(worker)
        for w in worker:
            while (current_diff_index < len(dp) and w >= dp[current_diff_index][0]):
                if current_diff_index == 0 and w >= dp[0][0]:
                    print('max_profit_index = %d' % max_profit_index)
                    max_profit_index = 0

                print('worker %d, difficulty %d' % (w, dp[current_diff_index][0]))
                if dp[current_diff_index][1] > dp[max_profit_index][1]:
                    max_profit_index = current_diff_index

                current_diff_index += 1
                print('-- index = %d', current_diff_index)

            print('max profit_index = %d' % max_profit_index)
            print('-----------------------')
            if max_profit_index >= 0:
                print('add %d' % dp[max_profit_index][1])
                max_profit_sum += dp[max_profit_index][1]
        print(max_profit_sum)
        return max_profit_sum


# print(Solution().maxProfitAssignment(difficulty=[2,4,6,8,10], profit=[10,20,30,40,50], worker=[4,5,6,7]) == 100)
# print(Solution().maxProfitAssignment(difficulty=[10], profit=[10], worker=[7]) == 0)
# print(Solution().maxProfitAssignment(difficulty=[2, 10], profit=[10, 1000], worker=[7, 10]) == 1010)
# print(Solution().maxProfitAssignment(difficulty=[2, 10], profit=[1000, 10], worker=[7, 10]) == 2000)
# print(Solution().maxProfitAssignment(difficulty=[13,37,58], profit=[4,90,96], worker=[34,73,45]) == 190)
print(Solution().maxProfitAssignment(difficulty=[66,1,28,73,53,35,45,60,100,44,59,94,27,88,7,18,83,18,72,63], profit=[66,20,84,81,56,40,37,82,53,45,43,96,67,27,12,54,98,19,47,77], worker=[61,33,68,38,63,45,1,10,53,23,66,70,14,51,94,18,28,78,100,16]) == 1392)
