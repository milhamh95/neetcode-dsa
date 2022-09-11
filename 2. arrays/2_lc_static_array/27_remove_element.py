# https://leetcode.com/problems/remove-element/

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0

        ctr = 0
        for x in nums:

            if x != val:
                nums[ctr] = x
                ctr += 1


        print("nums:", nums)

        return ctr
