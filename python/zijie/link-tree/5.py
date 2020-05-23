# 环形链表 II
# 给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

# 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

# 说明：不允许修改给定的链表。


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


import collections

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        node_dict = collections.OrderedDict() 
        while head:
            if head in node_dict.keys():
                return head
            else:
                node_dict[head] = len(node_dict.keys())
                head = head.next