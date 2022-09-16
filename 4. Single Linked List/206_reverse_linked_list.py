# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # iterative
        # time -> O(n) linear time
        # space -> O(1) constant space
        prev = None
        cur_node = head

        while cur_node:
            next_node = cur_node.next
            cur_node.next = prev
            prev = cur_node
            cur_node = next_node

        return prev

        # recursive
#         if head is None or head.next is None:
#             return head

#         newHead = self.reverseList(head.next)
#         nextHead = head.next
#         nextHead.next = head
#         head.next = None

#         return newHead
