# https://leetcode.com/problems/concatenation-of-array/

from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        # solution 1
        return nums + nums

# solution
#         lenNums = len(nums)
#         newNum = [0] * (lenNums * 2)

#         for i in range(0, lenNums):
#             newNum[i] = nums[i]
#             newNum[i + lenNums] = nums[i]

#         return newNum
