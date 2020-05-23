# 两数相加
# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

# 示例：

# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = None
        header = None
        carry = 0
        while l1 or l2:
            if l1 and l2:
                value = l1.val + l2.val + carry
                l1 = l1.next
                l2 = l2.next
            elif l1:
                value = l1.val + carry
                l1 = l1.next
            else:
                value = l2.val + carry
                l2 = l2.next
            carry = int(value / 10)
            v = value % 10
            node = ListNode(v)
            if result:
                result.next = node
                result = node
            else:
                header = node
                result = node
        if carry > 0:
            result.next = ListNode(carry)

        return header

n1 = ListNode(2)
n2 = ListNode(4)
n1.next = n2
n3 = ListNode(3)
n2.next = n3
n7 = ListNode(3)
n3.next = n7
n7.next = None

n4 = ListNode(5)
n5 = ListNode(6)
n4.next = n5
n6 = ListNode(4)
n5.next = n6
n6.next = None

print(Solution().addTwoNumbers(n1, n4))