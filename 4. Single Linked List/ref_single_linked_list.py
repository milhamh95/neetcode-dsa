# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

# create node
from operator import index, ne


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
        self.insert_at_middle(0, data)

    def insert_at_end(self, val):
        # send the size of the linked list
        # so in the loop, cur_loop will saved
        # the last node on linked list
        self.insert_at_middle(self.size, val)

    def insert_at_middle(self, idx, val):
        if idx > self.size or \
            (self.size > 0 and idx < 0):
            print("index is out of range")
            return

        cur_node = self.head
        new_node = Node(val)

        # idx = 0 -> insert at beginning
        # self.size == 0 and idx == -1 -> insert at the end
        if (idx == 0) or (self.size == 0 and idx == -1):
            new_node.next = cur_node
            self.head = new_node
            self.size += 1
            return

        # increase idx when insert node at the end of linke list
        # when self.size != 0
        if idx == self.size - 1:
            idx += 1

        # # goal -> we want move cur_node before idx - 1
        for _ in range(idx - 1):
            # move cur_node to next position
            cur_node = cur_node.next
        new_node.next = cur_node.next
        cur_node.next = new_node

        self.size += 1

    def print(self):
        if self.head == None:
            print("Linked List is empty")
            return

        elems = []
        cur_node = self.head
        while cur_node:
            elems.append(cur_node.val)
            cur_node = cur_node.next

        print(f"elems = {elems}, size = {self.size}")

    def get_head(self):
        self.get_by_index(0)

    def get_end(self):
        self.get_by_index(self.size - 1)

    def get_by_index(self, idx):
        if self.size == 0 or idx > self.size - 1 or idx < 0:
            print("index is out of range")
            return

        cur_node = self.head
        for _ in range(idx):
            cur_node = cur_node.next

        print(f"index = {idx} -> {cur_node.val}")

    def remove_by_index(self, idx):
        if self.size == 0 or idx > self.size - 1 or idx < 0:
            print("index is out of range")
            return

        if idx == 0:
            cur_node = self.head
            self.head = cur_node.next
            cur_node.next = None
            self.size -= 1
            return

        cur_node = self.head

        # prev_node = None
        # for _ in range(idx):
        #     prev_node = cur_node
        #     cur_node = cur_node.next

        # prev_node.next = cur_node.next
        # cur_node.next = None

        for _ in range(idx - 1):
            cur_node = cur_node.next

        cur_node.next = cur_node.next.next

        self.size -= 1

    def remove_end(self):
        self.remove_by_index(self.size - 1)

    def remove_beginning(self):
        self.remove_by_index(0)

    def modify_at_index(self, idx, val):
        if self.size == 0 or idx > self.size - 1 or idx < 0:
            print("index is out of range")
            return

        cur_node = self.head
        for _ in range(idx):
            cur_node = cur_node.next

        cur_node.val = val

    def modify_at_beginning(self, val):
        self.modify_at_index(0, val)

    def modify_at_end(self, val):
        self.modify_at_index(self.size - 1, val)



ll = LinkedList()

ll.insert_at_end(234)
ll.print()

ll.insert_at_end(23)
ll.print()

ll.insert_at_end(80)
ll.print()

ll.insert_at_middle(2, 107)
ll.print()

# ll.modify_at_end(384975)
# ll.print()

# # ll.get_head()
# # ll.get_by_index(1)
# # ll.get_by_index(0)
# # ll.get_end()
# ll.remove_beginning()
# ll.print()

# ll.remove_end()
# ll.print()

# ll.remove_by_index(2)
# ll.print()

# ll.insert_at_end(28233)
# ll.print()
# ll.get_end()
# ll.insert_at_beginning(3098)
# ll.insert_at_middle(1,90)

# ll.print_size()
# ll.get_by_index(2)
# ll.remove_by_index(1)
# ll.print()
# ll.print_size()
# ll.remove_end()
# ll.print()
# ll.print_size()
# ll.remove_beginning()
# ll.print()
# ll.print_size()
# ll.modify_at_index(1, 104)
# ll.remove_end()
# ll.print()
# ll.print_size()

