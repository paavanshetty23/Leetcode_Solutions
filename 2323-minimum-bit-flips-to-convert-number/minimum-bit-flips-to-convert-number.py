class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        
        res = start^goal
        res = bin (res)
        res =res.count('1')
        return res