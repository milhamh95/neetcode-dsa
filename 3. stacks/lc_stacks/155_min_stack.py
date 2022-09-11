# https://leetcode.com/problems/min-stack/

class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []


    def push(self, val: int) -> None:
        self.stack.append(val)

        # pick the last element of minStack
        # compare with val
        # if last element of minStack <= val
        # insert it to minStack
        if len(self.minStack) > 0:
            lastElem = self.minStack[-1]

            if val <= lastElem:
                self.minStack.append(val)

        else:
            self.minStack.append(val)

    def pop(self) -> None:
        elem = self.stack.pop()
        if elem == self.minStack[-1]:
            self.minStack.pop()


    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1]

        return 0


    def getMin(self) -> int:
        if len(self.stack) > 0 and len(self.minStack) > 0:
            return self.minStack[-1]

        return 0



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
