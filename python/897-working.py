# 给定一个树，按顺序重新排列树，使树中最左边的结点现在是树的根，并且每个结点没有左子结点，只有一个右子结点。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from list_2_node import TreeNode, list_2_node

class Solution:
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        new_node = None
        self.down_tree(root, new_node)
        return new_node
        

    def down_tree(self, root, new_node):
        while root.left != None and root.right != None:
            if root.left:
                self.down_tree(root.left, new_node)

                node = TreeNode(x = root.x)
                if not new_node:
                    new_node = new_node
                else:
                    new_node.right = node
                    new_node = node

            if root.right:
                self.down_tree(root.right, new_node)
                new_node.right = TreeNode(x = root.right.x)
                new_node = new_node.right

l = [5,3,6,2,4,None,8,1,None,None,None,7,9]
root = list_2_node(l)
print(Solution().increasingBST(root=root))