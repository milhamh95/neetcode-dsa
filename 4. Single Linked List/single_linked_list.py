# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

# create node
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# create linked list node
class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert_at_beginning(self, data):
        node = Node(data)

        if self.head == None:
            self.head = node
            self.size += 1
            return

        node.next = self.head
        self.head = node
        self.size += 1

    def insert_at_end(self, val):
        node = Node(val)
        cur_node = self.head

        # if there is no node in linked list
        if cur_node is None:
            self.head = node
            self.size += 1
            return

        # if there are nodes in linked list
        while cur_node:
            if cur_node.next == None:
                cur_node.next = node
                self.size += 1
                return

            cur_node = cur_node.next

    def print(self):
        if self.head == None:
            print("Linked List is empty")
            return

        elems = []
        cur_node = self.head
        while cur_node:
            elems.append(cur_node.val)
            cur_node = cur_node.next

        print(elems)

    def print_size(self):
        print(f"size: {self.size}")

    def get_by_index(self, idx):
        if idx > (self.size - 1) or idx < 0:
            print("index is out of range")
            return

        ctr = 0
        cur_node = self.head

        while ctr <= idx:
            if ctr == idx:
                print(f"idx = {idx}, val = {cur_node.val}")
                return

            cur_node = cur_node.next
            ctr += 1

    def remove_by_index(self, idx):
        if idx > (self.size - 1) or idx < 0:
            print("index is out of range")

        ctr = 0
        prev = None
        cur_node = self.head

        while ctr <= idx:
            if ctr == idx:
                prev.next = cur_node.next
                self.size -= 1
                return

            prev = cur_node
            cur_node = cur_node.next
            ctr =+ 1

    def remove_end(self):
        if self.size == 0:
            print("linked list is empty")
            return

        ctr = 0

        cur_node = self.head
        while ctr <= self.size - 2:
            if ctr == self.size - 2:
                cur_node.next = None
                self.size -= 1
                return

            cur_node = cur_node.next
            ctr += 1

    def remove_beginning(self):
        if self.size == 1:
            self.head = None;
            self.size = 0
            return

        self.head = self.head.next
        self.size -= 1

    def modify_at_index(self, idx, val):
        if (idx < 0) or (idx > self.size - 1):
            print("index is out of range")

        ctr = 0
        cur_node = self.head
        while ctr <= idx:
            if ctr == idx:
                cur_node.val = val
                return

            ctr += 1
            cur_node = cur_node.next

    def modify_at_beginning(self, val):
        if self.size == 0:
            print("linked list is empty")
            return

        self.head.val = val

    def modify_at_end(self, val):
        if self.size == 0:
            print("linked list is empty")
            return

        cur_node = self.head
        while cur_node:
            if cur_node.next == None:
                cur_node.next = node
                self.size += 1
                return

            cur_node = cur_node.next



ll = LinkedList()
ll.insert_at_beginning(1)
ll.insert_at_beginning(2)
ll.insert_at_end(4)
ll.insert_at_end(10)
# ll.print()
# ll.print_size()
# ll.get_by_index(2)
# ll.remove_by_index(1)
# ll.print()
# ll.print_size()
# ll.remove_end()
# ll.print()
# ll.print_size()
# ll.remove_beginning()
ll.print()
ll.print_size()
ll.modify_at_index(1, 104)
ll.print()
ll.print_size()

