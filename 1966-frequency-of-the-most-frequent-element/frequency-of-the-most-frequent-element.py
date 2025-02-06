class Solution(object):
    def maxFrequency(self, nums, k):
        nums.sort()

        l, r = 0, 0
        res, total = 0, 0

        while r < len(nums):
            total += nums[r]

            while nums[r] * (r - l + 1) > total + k:
                total -= nums[l]
                l += 1

            res = max(res, r - l + 1)  # This should be inside the main loop
            r += 1  # This should also be inside the main loop
        
        return res  # Ensure to return the result
