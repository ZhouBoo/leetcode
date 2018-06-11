
from list_2_node import TreeNode
from list_2_node import list_2_node

class Solution:
    
    def __init__(self, *args, **kwargs):
        pass

    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        tail_node = None
        self.deep(root, tail_node)

    def deep(self, root, last):
        if not root:
            return

        if (not root.left) and (not root.right):
            last = root
            return

        left = root.left
        right = root.right
        left_last = None
        right_last = None

        print(root.val)
        if left:
            self.deep(left, left_last)
            root.left = None
            root.right = left
            last = left_last

        if right:
            self.deep(right, right_last)
            if left_last:
                left_last.right = right
            last = right_last
        

lists = [1,2,5,3,4,None,6]
nodes = list_2_node(lists)

Solution().flatten(nodes)

# head = nodes
# while(head.right):
#     # print(nodes.val)
#     head = head.right