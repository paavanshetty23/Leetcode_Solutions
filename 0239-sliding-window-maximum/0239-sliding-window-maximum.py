from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Deque to store indices of elements in the current window
        dq = deque()
        result = []
        
        for i in range(len(nums)):
            # Remove elements from the front of the deque if they are out of the current window
            if dq and dq[0] < i - k + 1:
                dq.popleft()
            
            # Remove elements from the back of the deque if they are smaller than the current element,
            # because they won't be the maximum for this or future windows
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            
            # Add the current element's index to the deque
            dq.append(i)
            
            # Once we have a complete window, add the maximum to the result
            if i >= k - 1:
                result.append(nums[dq[0]])  # The element at the front of the deque is the maximum
        
        return result