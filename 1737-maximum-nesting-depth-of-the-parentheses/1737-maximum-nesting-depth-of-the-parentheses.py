from collections import deque

class Solution:
    def maxDepth(self, s: str) -> int:
        max_val = 0
        current_depth = 0
        for char in s:
            if char == '(':
                current_depth += 1
                max_val = max(max_val, current_depth)
            elif char == ')':
                current_depth -= 1
        return max_val

        
        