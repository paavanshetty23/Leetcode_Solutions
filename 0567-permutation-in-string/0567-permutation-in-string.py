from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        right = len(s1) - 1
        s1_counter = Counter(s1)
        
        while right < len(s2):
           
            if s1_counter == Counter(s2[left:right+1]):
                return True
            left += 1
            right += 1
            
        return False
