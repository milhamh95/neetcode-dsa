# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        linkedlist = ListNode()
        cur = linkedlist

        while list1 and list2:
            if list1.val < list2.val:

                # set linkedlist.next dengan list1 node
                linkedlist.next = list1

                # pindah list1 ke node list1 selanjutnya
                list1 = list1.next
            else:

                # set linkedlist.next dengan list2 node
                linkedlist.next = list2

                # pindah list2 ke node list2 selanjutnya
                list2 = list2.next

            # pindah linkedlist ke node linkedlist selanjutnya
            # yang sudah diinsert ketika pengecekan val1 dan val2
            linkedlist = linkedlist.next

        # pada satu tahap ada saia node di list1 atau list2
        if list1:
            linkedlist.next = list1
        elif list2:
            linkedlist.next = list2

        return cur.next
