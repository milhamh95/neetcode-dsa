class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert_at_beginning(self, val):
        new_node = Node(val)
        self.head = new_node
        self.size += 1

        if self.size == 1:
            self.tail = self.head

    def insert_at_end(self, val):
        new_node = Node(val)
        self.tail.next = new_node
        self.tail = self.tail.next
        self.size += 1

        if self.size == 1:
            self.head = self.tail

    def insert_at_middle(self, idx, val):
        if idx > (self.size - 1) or idx < 0:
            print("index is out of range")
            return

        if self.size == 0:
            self.insert_at_beginning(val)
            return

        new_node = Node(val)
        cur_node = self.head

        for _ in range(idx - 1):
            cur_node = cur_node.next

        new_node.next = cur_node.next
        cur_node.next = new_node

    def print(self):
        elems = []

        cur_node = self.head
        while cur_node:
            elems.append(cur_node.val)
            cur_node = cur_node.next

        print(f"elem = {elems} with size = {self.size}")

    def print_head(self):
        if self.size == 0:
            print("linked list is empty")
            return

        print(f"head = {self.head.val}")

    def print_tail(self):
        if self.size == 0:
            print("linked list is empty")
            return

        print(f"tail = {self.tail.val}")

    def modify_at_beginning(self, val):
        if self.size == 0:
            print("linked list is empty")
            return

        self.head.val = val

    def modify_at_end(self, val):
        if self.size == 0:
            print("linked list is empty")
            return

        self.tail.val = val

    def remove_beginning(self):
        if self.size == 0:
            print("linked list is empty")
            return

        if self.size == 1:
            self.head = None
            self.tail = None
            self.size = 0
            return

        next_node = self.head.next
        self.head = next_node
        self.size -= 1

        if self.size == 1:
            self.tail = self.head

    def remove_end(self):
        if self.size == 0:
            print("linked list is empty")
            return

        if self.size == 1:
            self.head = None
            self.tail = None
            self.size = 0
            return

        second_last = self.head
        while second_last.next.next:
            second_last = second_last.next

        second_last.next = None
        self.tail = second_last
        self.size -= 1

ll = LinkedList()
ll.insert_at_beginning(103)
ll.insert_at_end(31)
ll.insert_at_end(98)
ll.insert_at_end(23)
ll.insert_at_end(41)
ll.insert_at_middle(1, 1009)
ll.print()
