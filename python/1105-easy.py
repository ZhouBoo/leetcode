# 1103. 二叉树寻路
# 在一棵无限的二叉树上，每个节点都有两个子节点，树中的节点 逐行 依次按 “之” 字形进行标记。
# 如下图所示，在奇数行（即，第一行、第三行、第五行……）中，按从左到右的顺序进行标记；
# 而偶数行（即，第二行、第四行、第六行……）中，按从右到左的顺序进行标记。

import math

class Solution:
    def pathInZigZagTree(self, label: int) -> [int]:

        start = 0#2 ** n
        end = 0#start + n - 1
        level = 1
        while True:
            start = 2 ** (level - 1)
            end = start * 2 - 1
            print(start, end)
            if start <= label and end >= label:
                break
            level += 1
        l = label
        res = [label]
        while level > 1:
            is_left = level % 2 == 0 
            start = 2 ** (level - 1)
            end = start * 2 - 1
            tree_node = end - label if is_left else label - start
            up_idx = math.ceil(tree_node) / 2.0
            label = 

print(Solution().pathInZigZagTree(14))