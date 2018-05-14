import array
import list_2_node as ln
from list_2_node import TreeNode

class Solution(object):

    def __init__(self):
        self.values = []
        self.p_path = []
        self.q_path = []
        self.ancestor = None

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        # if root == None or self.ancestor != None:
        #     print("return root val == %d or self.ancestor = %r" % (root.val, self.ancestor))
        #     return None

        # # if len(self.values) <= 0:
        # #     self.values.append(root.val)

        # # if root.val == p and (q != p or len(self.p_path) ==  0):
        # #     self.p_path = list(self.values)
        # #     print("find p = %d", p)
        # # elif root.val == q:
        # #     self.q_path = list(self.values)
        # #     print("find q = %d", q)

        # # if len(self.p_path) > 0 and len(self.q_path) > 0:
        # #     print("self.q_path = %r" % self.q_path)
        # #     print("self.p_path = %r" % self.p_path)
        # #     if len(self.p_path) == len(self.q_path):
        # #         self.p_path.pop()
        # #         self.q_path.pop()

        # #     while len(self.q_path) > 0:
        # #         n = self.q_path.pop()
        # #         try:
        # #             index = self.p_path.index(n)
        # #             self.ancestor = n
        # #             print("---- find %d at index = %d", n, index)
        # #             return self.ancestor
        # #         except ValueError:
        # #             print("---- not find %d ", n)
        # #             continue

        #     # print("return None")
        #     # return None

        # if root.left != None:
        #     print('left = %d', root.left.val)
        #     self.values.append(root.left.val)
        #     self.lowestCommonAncestor(root.left, p, q)
        # else :
        #     print('left = none')

        # if root.right != None:
        #     print('right = %d', root.right.val)
        #     self.values.append(root.right.val)
        #     self.lowestCommonAncestor(root.right, p, q)
        # else :
        #     print('right = none')

        # # self.values.pop()
        
        # return self.ancestor
        parents = {}
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left:
                parents[node.left] = node
                stack.append(node.left)
            if node.right:
                parents[node.right] = node
                stack.append(node.right)
        node1, node2 = p, q
        while node1 != node2:
            print(node1)
            node1 = parents[node1] if node1 != root else q
            node2 = parents[node2] if node2 != root else p
        return node1

if __name__ == '__main__':

    # lists = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    # p = 5
    # q = 1

    # lists = [1, 2]
    # p = 1
    # q = 2

    # lists = [9, -1, -4, 10, 3, None, None, None, 5]
    # p = 3
    # q = 5

    # lists = [37,-34,-48,None,-100,-100,48,None,None,None,None,-54,None,-71,-22,None,None,None,8]
    # p = -100
    # q = -100

    # lists = [-1,0,3,-2,4,None,None,8]
    # p = 8
    # q = 4

    # 37
    # -34 -48
    # n -100 | -100 48
    # n n n n | -54 n -71 -22
    # n n n n 8

    # lists = [37,-34,-48,None,-100,-100,48,None,None,None,None,-54,None,-71,-22,None,None,None,8]
    # p = -100
    # q = -71


    lists = [-64,12,18,-4,-53,None,76,None,-51,None,None,-93,3,None,-31,47,None,3,53,-81,33,4,None,-51,-44,-60,11,None,None,None,None,78,None,-35,-64,26,-81,-31,27,60,74,None,None,8,-38,47,12,-24,None,-59,-49,-11,-51,67,None,None,None,None,None,None,None,-67,None,-37,-19,10,-55,72,None,None,None,-70,17,-4,None,None,None,None,None,None,None,3,80,44,-88,-91,None,48,-90,-30,None,None,90,-34,37,None,None,73,-38,-31,-85,-31,-96,None,None,-18,67,34,72,None,-17,-77,None,56,-65,-88,-53,None,None,None,-33,86,None,81,-42,None,None,98,-40,70,-26,24,None,None,None,None,92,72,-27,None,None,None,None,None,None,-67,None,None,None,None,None,None,None,-54,-66,-36,None,-72,None,None,43,None,None,None,-92,-1,-98,None,None,None,None,None,None,None,39,-84,None,None,None,None,None,None,None,None,None,None,None,None,None,-93,None,None,None,98]

            #                        -64
            #                 12           18 
            #             -4      53   n      76
            #          n    -51   n n       n  -31
            #            3     53            n    n
            #     n n  -35 -64  26 -81
            # n n  n n 72 n n n -70 17 -4 n
            #         n 92      n n -67 n
                
    p = TreeNode(74)
    q = TreeNode(-40)

    tree_node = ln.list_2_node(lists)
    s = Solution()
    print(p)
    print(q)
    n = s.lowestCommonAncestor(tree_node, p=p, q=q)
    print(n)
