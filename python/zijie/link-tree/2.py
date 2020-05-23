# 反转链表
# 反转一个单链表。

# 示例:

# 输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        last = None
        while head:
            next = head.next
            if not last:
                last = head
                head = next
                last.next = None
            else:
                head.next = last
                last = head
                head = next
        return last


n1 = ListNode(1)
n2 = ListNode(2)
n1.next = n2
n3 = ListNode(3)
n2.next = n3
n4 = ListNode(4)
n3.next = n4
n5 = ListNode(5)
n4.next = n5
n5.next = None

n = Solution().reverseList(n1)

while n:
    print(n.val)
    n = n.next