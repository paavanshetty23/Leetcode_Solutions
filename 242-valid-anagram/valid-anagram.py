class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hms, hmt = {}, {}
        
        for i in range(len(s)):
            hms[s[i]] = 1 + hms.get(s[i], 0)
            hmt[t[i]] = 1 + hmt.get(t[i], 0)

        for c in hms:
            if hms[c] != hmt.get(c, 0):
                return False

        return True