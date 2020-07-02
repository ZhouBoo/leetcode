# 二叉树的锯齿形层次遍历
# 给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

# 例如：
# 给定二叉树 [3,9,20,null,null,15,7],

#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回锯齿形层次遍历如下：

# [
#   [3],
#   [20,9],
#   [15,7]
# ]

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> [[int]]:
        result = []
        if not root:
            return result
        array = [root]
       
        while True:
            temp_array = []
            next_array = []
            for node in array:
                temp_array.append(node)
                if node.left:
                    next_array.append(node.left)
                if root.right:
                    next_array.append(node.right)    
            result.append(temp_array)
            if not next_array:
                return result
            else:
                array = reversed(next_array)
                



def quicksort(nums, start, end):
    if start >= end:
        return
    index = partial(nums, start, end)
    quicksort(nums, start, index - 1)
    quicksort(nums, index + 1, end)
    return nums


def partial(nums, start, end):
    ## 左找到比 val 大  右找到比 val 小
    e = end
    val = nums[e]
    while start < e:
        if nums[start] <= val:
            start += 1
            continue
        if nums[e] >= val:
            e -= 1
            continue
        nums[e], nums[start] = nums[start], nums[e]
        start += 1
        e -= 1
    nums[start], nums[end] = nums[end], nums[start]
    return start


a = [10,3,17,8,5,2,1,9,5,4]

print(quicksort(a, 0, len(a) - 1))

            
        