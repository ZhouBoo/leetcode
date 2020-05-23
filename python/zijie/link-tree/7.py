# 合并K个排序链表
# 合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

# 示例:

# 输入:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# 输出: 1->1->2->3->4->4->5->6


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

#####
## timeout 1

    # def mergeKLists(self, lists: [ListNode]) -> ListNode:
    #     head = None
    #     result = None
    #     list_sort = lists
    #     while True:
    #         all_none = True
    #         min_node = None
    #         min_index = -1
    #         for (index, l) in enumerate(list_sort):
    #             if l:
    #                 all_none = False
    #                 if min_node is None:
    #                     min_node = l
    #                     min_index = index
    #                 else:
    #                     if min_node.val > l.val:
    #                         min_node = l
    #                         min_index = index 
    #         if all_none:
    #             break
    #         else:
    #             if head is None:
    #                 head = min_node
    #                 result = min_node
    #             else:
    #                 head.next = min_node
    #                 head = head.next
    #             list_sort[min_index] = list_sort[min_index].next
    #             print('min_node :', min_node, "| min_index = ", min_index)
    #     return result


#####
## timeout 2
        def mergeKLists(self, lists: [ListNode]) -> ListNode:
            if len(lists) == 0:
                return []
            if len(lists) == 1:
                return lists[0]
            result = lists[0]
            for l in lists[1:]:
                result = self.merge(result, l)
            return result


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


n1 = ListNode(1)
n2 = ListNode(4)
n1.next = n2
n3 = ListNode(5)
n2.next = n3
n3.next = None

n4 = ListNode(1)
n5 = ListNode(3)
n4.next = n5
n6 = ListNode(4)
n5.next = n6
n6 = None

n7 = ListNode(2)
n8 = ListNode(6)
n7.next = n8
n8.next = None

n = Solution().mergeKLists([n1, n4, n7])

while n:
    print(n.val)
    n = n.next