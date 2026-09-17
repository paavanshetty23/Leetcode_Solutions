class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hs = set()
        for n in nums:
            hs.add(n)

        if  len(hs)!=len(nums):
            return True
        return False