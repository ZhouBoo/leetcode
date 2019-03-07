class Solution:
    def maxProfitAssignment(self, difficulty, profit, worker):
        current_diff_index = 0
        max_profit_index = 0
        max_profit_sum = 0
        for w in worker:
            while (w >= difficulty[current_diff_index]):
                if current_diff_index == len(difficulty) - 1:
                    break

                if profit[current_diff_index] > profit[current_diff_index - 1]:
                    max_profit_index = current_diff_index - 1
                else:
                    max_profit_index = current_diff_index

                current_diff_index += 1

            print('max_ profit_index = %d' % max_profit_index)
            max_profit_sum += profit[max_profit_index]
        return max_profit_sum


print(Solution().maxProfitAssignment(difficulty= [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]))