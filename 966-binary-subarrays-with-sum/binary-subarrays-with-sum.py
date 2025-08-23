class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        # Helper function that counts subarrays with sum AT MOST k
        # This is your original code, just wrapped in a function.
        def atMost(k: int) -> int:
            if k < 0:
                return 0
            
            l, summ, count = 0, 0, 0
            for r in range(len(nums)):
                summ += nums[r]
                while summ > k:
                    summ -= nums[l]
                    l += 1
                # This counts all subarrays ending at r with sum <= k
                count += (r - l + 1)
            return count
            
        # The main logic: count(goal) - count(goal - 1)
        return atMost(goal) - atMost(goal - 1)