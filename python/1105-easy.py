# 1103. 二叉树寻路
# 在一棵无限的二叉树上，每个节点都有两个子节点，树中的节点 逐行 依次按 “之” 字形进行标记。
# 如下图所示，在奇数行（即，第一行、第三行、第五行……）中，按从左到右的顺序进行标记；
# 而偶数行（即，第二行、第四行、第六行……）中，按从右到左的顺序进行标记。

import math

class Solution:
    def pathInZigZagTree(self, label: int) -> [int]:
        level = 0
        l = label
        while l > 0:
            l = int(l / 2)
            level += 1

        start = 2 ** (level - 1)
        end = start * 2 - 1
        is_left = level % 2 == 0 
        node_index = int((end - label if is_left else label - start) / 2)
        res = [label]
        level -= 1
        while level > 0:
            start = 2 ** (level - 1)
            end = start * 2 - 1
            is_left = level % 2 == 0
            num = end - node_index if is_left else start + node_index
            res.insert(0, num)
            node_index = int(node_index / 2)
            level -= 1
        return res


print(Solution().pathInZigZagTree(14))
print(Solution().pathInZigZagTree(26))