
from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # max_prod_ending_here tracks the maximum product of a subarray ending at the current position.
        # min_prod_ending_here tracks the minimum product of a subarray ending at the current position.
        # These are crucial because a negative number multiplied by a negative minimum can become a new maximum.
        max_prod_ending_here = nums[0]
        min_prod_ending_here = nums[0]
        
        # result stores the overall maximum product found across all subarrays.
        result = nums[0]

        # Iterate through the array starting from the second element
        for i in range(1, len(nums)):
            num = nums[i]

            # If the current number is negative, multiplying it by the current max_prod_ending_here
            # would make it a smaller (more negative) number, and multiplying it by
            # min_prod_ending_here would make it a larger (more positive) number.
            # So, we swap max_prod_ending_here and min_prod_ending_here to correctly
            # calculate the next maximum and minimum products.
            if num < 0:
                max_prod_ending_here, min_prod_ending_here = min_prod_ending_here, max_prod_ending_here
            
            # Update max_prod_ending_here:
            # It can either be the current number itself (starting a new subarray)
            # or the product of the current number and the previous max_prod_ending_here.
            max_prod_ending_here = max(num, max_prod_ending_here * num)
            
            # Update min_prod_ending_here:
            # It can either be the current number itself
            # or the product of the current number and the previous min_prod_ending_here.
            min_prod_ending_here = min(num, min_prod_ending_here * num)
            
            # Update the global result with the maximum product found so far.
            result = max(result, max_prod_ending_here)
            
        return result