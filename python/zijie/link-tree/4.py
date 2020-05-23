# 排序链表
# 在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。

# 示例 1:

# 输入: 4->2->1->3
# 输出: 1->2->3->4
# 示例 2:

# 输入: -1->5->3->4->0
# 输出: -1->0->3->4->5


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # middle
        walk_p = head
        # end
        run_p = head
        while run_p:
            walk_p = walk_p.next
            if run_p.next:
                run_p = run_p.next 
                if run_p.next:
                    run_p = run_p.next
                else:
                    break
            else:
                break
            
        left = self.run(head, walk_p)
        right = self.run(walk_p.next, run_p)
        return self.merge(left, right)

    def run(self, head, end):
        if head == end:
            return head
        if head.next == end:
            if head.val < end.val:
                return head
            else:
                head.next = None
                end.next = head
                return end
        walk_p = head
        run_p = head
        while run_p.next != end:
            walk_p = walk_p.next
            if run_p.next == end:
                run_p = run_p.next
                break
            elif run_p.next.next == end:
                run_p = run_p.next.next
                break
            else:
                run_p = run_p.next.next
        sortleft = self.run(head, walk_p)
        sortright = self.run(walk_p, end)
        return self.merge(sortleft, sortright)

    def merge(self, left, right):
        head = None
        result = None
        while left or right:
            if left and right:
                if left.val > right.val:
                    if head:
                        head.next = right
                        head = head.next
                    else:
                        head = right
                        result = head
                    right = right.next 
                else:
                    if head:
                        head.next = left
                        head = head.next
                    else:
                        head = left
                        result = head
                    left = left.next
            elif left:
                if head:
                    head.next = left
                    head = head.next
                else:
                    head = left
                    result = left
                left = left.next
            else:
                if head:
                    head.next = right
                    head = head.next
                else:
                    head = right
                    result = right
                right = right.next
        return result
                    
            
        
n1 = ListNode(2)
n2 = ListNode(4)
n1.next = n2
n3 = ListNode(3)
n2.next = n3
n7 = ListNode(6)
n3.next = n7
n7.next = None

n4 = ListNode(5)
n5 = ListNode(6)
n4.next = n5
n6 = ListNode(4)
n5.next = n6
n6.next = None

# merge right
# n = Solution().merge(n1, n4)

n = Solution().sortList(n1)

while n:
    print(n.val)
    n = n.next