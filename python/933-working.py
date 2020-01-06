# 写一个 RecentCounter 类来计算最近的请求。
# 它只有一个方法：ping(int t)，其中 t 代表以毫秒为单位的某个时间。
# 返回从 3000 毫秒前到现在的 ping 数。
# 任何处于 [t - 3000, t] 时间范围之内的 ping 都将会被计算在内，包括当前（指 t 时刻）的 ping。
# 保证每次对 ping 的调用都使用比之前更大的 t 值。

# 输入：inputs = ["RecentCounter","ping","ping","ping","ping"], inputs = [[],[1],[100],[3001],[3002]]
# 输出：[null,1,2,3,3]


# class RecentCounter:
#     def __init__(self):
#         pass
    
#     def ping(self, t):
#         """
#         :type t: int
#         :rtype: int
#         """


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
# 假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
# 例如输入前序遍历序列{1,2,4,7,3,5,6,8}和
# 中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
class Solution:
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if len(pre) <= 0:
            return None
        for index in pre:
            