# 反转一个单链表。

# 示例:
# 输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return 'val = %d' % self.val

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        h = head
        last = None
        while h:
            ch = h.next
            h.next = last
            last = h
            h = ch


    def printAll(self, head: ListNode):
        h = head
        while h:
            print(h)
            h = h.next


if __name__ == "__main__":
    ln1 = ListNode(1)
    ln2 = ListNode(2)
    ln1.next = ln2
    ln3 = ListNode(3)
    ln2.next = ln3
    ln4 = ListNode(4)
    ln3.next = ln4
    ln5 = ListNode(5)
    ln4.next = ln5
    ln5.next = None

    s = Solution()
    # s.printAll(ln1)
    s.reverseList(ln1)
    s.printAll(ln5)
