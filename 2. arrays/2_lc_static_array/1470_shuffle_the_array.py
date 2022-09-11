# https://leetcode.com/problems/shuffle-the-array/

from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        newNums = []

        for i in range(0, n):
            newNums.append(nums[i])
            newNums.append(nums[i + n])

        return newNums
