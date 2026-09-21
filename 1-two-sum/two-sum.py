class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        hm = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in hm:
                return [hm[diff],i]
            hm[n]=i

        return
        