import math

class Solution(object):
    def minEatingSpeed(self, piles, h):
        
        left, right = 1, max(piles)
        res = right  
        
        while left <= right:
            mid = (left + right) // 2 
            hours = 0
            
            for p in piles:
                hours += math.ceil(p / mid)
            
            if hours <= h:
                res = mid  
                right = mid - 1
            else:
                left = mid + 1  
                
        return res 
