from wsgiref.util import request_uri


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert_at_front(self, val):
        if self.size == 0:
            self.head = ListNode(val)
            self.size += 1
            return

        cur_node = self.head

        new_node = ListNode(val)
        new_node.next = cur_node
        cur_node.prev = new_node

        self.head = new_node
        self.size += 1

    def insert_at_middle(self, idx, val):
        if idx < 0 or (idx > self.size - 1):
            print("index is out of range")
            return

        if idx == 0:
            self.insert_at_front(val)
            return

        new_node = ListNode(val)

        cur_node = self.head
        prev_node = None

        for _ in range(idx):
            prev_node = cur_node
            cur_node = cur_node.next

        new_node.next = cur_node
        cur_node.prev = new_node

        new_node.prev = prev_node
        prev_node.next = new_node

    def insert_at_end(self, val):
        if self.size == 0:
            self.head = ListNode(val)
            self.size += 1
            return

        cur_node = self.head
        while cur_node:
            if cur_node.next is None:
                new_node = ListNode(val)
                cur_node.next = new_node
                new_node.prev = cur_node
                self.size += 1
                return

            cur_node = cur_node.next

    def remove_beginning(self):
        if self.size == 0:
            print("linked list is empty")
            return

        if self.size == 1:
            self.head = None
            self.size -= 1
            return

        cur_node = self.head
        next_node = cur_node.next

        self.head = next_node
        cur_node.next = None
        next_node.prev = None
        self.size -= 1

    def remove_middle(self, idx):
        if self.size == 0:
            print("linked list is empty")
            return

        if idx < 0 or idx > (self.size - 1):
            print("index is out of range")
            return

        ctr = 0
        cur_node = self.head
        prev_node = None

        while ctr <= idx:
            if ctr == idx:
                next_node = cur_node.next

                cur_node.prev = None
                cur_node.next = None

                prev_node.next = next_node
                next_node.prev = prev_node

                self.size -= 1

                return

            prev_node = cur_node
            cur_node = cur_node.next
            ctr += 1

    def remove_end(self):
        if self.size == 0:
            print("linked list is empty")
            return

        if self.size == 1:
            self.head = None
            self.size -= 1
            return

        second_last = self.head
        last = None

        while second_last.next.next:
            second_last = second_last.next
            last = second_last.next

        second_last.next = None
        last.prev = None
        self.size -= 1

    def print(self):
        elems = []

        cur_node = self.head
        while cur_node:
            elems.append(cur_node.val)

            cur_node = cur_node.next

        print(f"elems = {elems}, size = {self.size}")


ll = LinkedList()
ll.insert_at_end(10)
ll.insert_at_end(30)
ll.insert_at_front(87)
ll.insert_at_end(81)
ll.insert_at_end(64)
ll.print()

ll.remove_beginning()
ll.remove_end()
ll.print()
