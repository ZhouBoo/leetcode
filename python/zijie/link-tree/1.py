# 合并两个有序链表
# 将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

# 示例：

# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, h1: ListNode, h2: ListNode) -> ListNode:
        head = None
        result = None
        while h1 != None or h2 != None:
            if h1 == None:
                print('h1 none')
                head.next = h2
                h2 = h2.next
                head = head.next
                continue
            if h2 is None:
                print('h2 none')
                head.next = h1
                h1 = h1.next
                head = head.next
                continue
            
            if h1.val > h2.val:
                print('h1 > h2')
                if head is None:
                    head = h2
                    result = h2
                else:
                    head.next = h2
                    head = head.next
                h2 = h2.next
            else:
                print('h1 <= h2')
                if head is None:
                    head = h1
                    result = h1
                else:
                    head.next = h1
                    head = head.next
                h1 = h1.next
        return result
        
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)

n1.next = n2
n2.next = None

n3.next = n4
n4.next = n5
n5.next = None

n = Solution().mergeTwoLists(n1, n3)

while n:
    print(n.val)
    n = n.next
