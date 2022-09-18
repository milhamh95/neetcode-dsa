class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index >= self.size or index < 0:
            return -1

        cur_node = self.head
        for _ in range(index):
            cur_node = cur_node.next

        return cur_node.val


    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)


    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)


    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return

        cur_node = self.head
        new_node = Node(val)

        if index == 0:
            new_node.next = cur_node
            self.head = new_node
            self.size += 1
            return

        print(self.size)
        print(index)

        for _ in range(index - 1):
            cur_node = cur_node.next

        new_node.next = cur_node.next
        cur_node.next = new_node
        self.size += 1


    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return

        if index == 0:
            self.head = self.head.next
            self.size -= 1
            return

        cur_node = self.head
        prev_node = None
        for _ in range(index):
            prev_node = cur_node
            cur_node = cur_node.next

        prev_node.next = cur_node.next
        cur_node.next = None

        self.size -= 1

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


obj = MyLinkedList()

obj.addAtHead(10)
obj.addAtHead(30)
obj.print()

# obj.addAtTail(10)
# obj.addAtTail(7)
# obj.addAtTail(3)
# obj.addAtTail(5)
# obj.addAtTail(98)
# obj.addAtTail(234)
# obj.print()

# print(obj.get(2))
# obj.deleteAtIndex(0)
# obj.print()

# obj.deleteAtIndex(4)
# obj.print()


# obj.addAtHead(1)
# obj.print()

# obj.addAtTail(3)
# obj.print()
# obj.addAtIndex(1,2)
# obj.print()

# print(obj.get(1))
# obj.deleteAtIndex(1)

# obj.print()

# print(obj.get(1))

