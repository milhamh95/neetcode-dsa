class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0

        # ctr will be increased if
        # prev num != cur num
        # min unique is 1
        ctr = 1

        for idx in range(1, len(nums), 1):
            if nums[idx] != nums[idx - 1]:
                nums[ctr] = nums[idx]
                ctr += 1

        print("nums:", nums)

        return ctr
