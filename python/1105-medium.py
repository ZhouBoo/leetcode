# 附近的家居城促销，你买回了一直心仪的可调节书架，打算把自己的书都整理到新的书架上。
# 你把要摆放的书 books 都整理好，叠成一摞：从上往下，第 i 本书的厚度为 books[i][0]，高度为 books[i][1]。
# 按顺序 将这些书摆放到总宽度为 shelf_width 的书架上。
# 先选几本书放在书架上（它们的厚度之和小于等于书架的宽度 shelf_width），然后再建一层书架。
# 重复这个过程，直到把所有的书都放在书架上。
# 需要注意的是，在上述过程的每个步骤中，摆放书的顺序与你整理好的顺序相同。
# 例如，如果这里有 5 本书，那么可能的一种摆放情况是：第一和第二本书放在第一层书架上，第三本书放在第二层书架上，第四和第五本书放在最后一层书架上。
# 每一层所摆放的书的最大高度就是这一层书架的层高，书架整体的高度为各层高之和。
# 以这种方式布置书架，返回书架整体可能的最小高度。

# 输入：books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], shelf_width = 4
# 输出：6
# 解释：
# 3 层书架的高度和为 1 + 3 + 2 = 6 。
# 第 2 本书不必放在第一层书架上。

# 动态规划，用 dp[i] 表示放置前 i 本书所需要的书架最小高度，初始值 dp[0] = 0，其他为最大值 1000*1000。
# 遍历每一本书，把当前这本书作为书架最后一层的最后一本书，将这本书之前的书向后调整，看看是否可以减少之前的书架高度。
# 状态转移方程为 dp[i] = min(dp[i] , dp[j - 1] + h)，其中 j 表示最后一层所能容下书籍的索引，h 表示最后一层最大高度。


class Solution:
    def minHeightShelves(self, books: [[int]], shelf_width: int) -> int:
        from functools import reduce
        levels = []
        max_height = 0
        for book in books:
            if not levels:
                levels.append([book])
                max_height = book[1]
            else:
                last_book = levels[-1][-1]
                # 先当成最后一层，计算高度
                max_height += book[1]
                if last_book[0] + book[0] <= shelf_width:
                    # 把上个移到这边来看看高度
                    # 排除最后一个最大的数
                    b = reduce(lambda x, y: max(x, y[1]), books[-1][:-1], 0)
                    # 包含最后一个数最大的数
                    b_c = max(b, last_book[1])
                    # 最后一个移入后的高度
                    n = max(last_book[1], book[1])

                    if b + n > b_c + book[1]:
                        levels.append([book])
                    else:
                        levels[-1] = books[-1][:-1]
                        levels.append([last_book, book])
                    max_height                    
                    

                else:
                    levels.append([book])

# 把上一个最后的元素吸收过来，查看是否能减少最大高度
# 如果能减少，则合并
# 否则
# 相同的应该优先在一起，并且有右结合性质
# 3 3 2
# 1 3 3 2
# print(Solution().minHeightShelves([[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], 4) )
# print(Solution().minHeightShelves([[7,3],[8,7],[2,7],[2,5]], 10) )
# print(Solution().minHeightShelves([[1,1],[2,3],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], 4) )
# print(Solution().minHeightShelves([[9,9],[5,4],[3,1],[1,5],[7,3]], 10) )