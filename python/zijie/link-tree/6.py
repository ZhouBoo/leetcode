# 相交链表
# 编写一个程序，找到两个单链表相交的起始节点。

# 如下面的两个链表：


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        # find tire
        acount = 0
        bcount = 0
        ha = headA
        hb = headB
        while ha or hb:
            if ha:
                acount += 1
                ha = ha.next
            if hb:
                bcount += 1
                hb = hb.next
        
        ha = headA
        hb = headB
        if acount > bcount:
            jumpa = acount - bcount
            while jumpa > 0:
                ha = ha.next
                jumpa -= 1
        else:
            jumpb = bcount - acount
            while jumpb > 0:
                hb = hb.next
                jumpb -= 1

        while ha or hb:
            if ha.val == hb.val:
                return ha
            else:
                ha = ha.next
                hb = hb.next
        
n1 = ListNode(4)
n2 = ListNode(1)
n1.next = n2
n3 = ListNode(8)
n2.next = n3
n7 = ListNode(4)
n3.next = n7
n8 = ListNode(5)
n7.next = n8
n8.next = None

n4 = ListNode(5)
n5 = ListNode(0)
n4.next = n5
n6 = ListNode(1)
n5.next = n6
n9 = ListNode(8)
n6.next = n9
n10 = ListNode(4)
n9.next = n10
n11 = ListNode(5)
n10.next = n11
n11.next = None


print(Solution().getIntersectionNode(n1, n4).val)