# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False

        stack = []
        mapP = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for ltr in s:
            openP = mapP.get(ltr, None)
            if openP == None:
                stack.append(ltr)
                continue

            if len(stack) > 0 and stack[len(stack) - 1] == openP:
                stack = stack[:len(stack) - 1]
                continue

            # closed parenthesis can't be in front
            return False

        return len(stack) == 0

