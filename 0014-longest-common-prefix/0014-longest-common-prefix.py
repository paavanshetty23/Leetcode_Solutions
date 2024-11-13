from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # If the list is empty, return an empty string
        if not strs:
            return ""
        
        # Start with the first string as the initial prefix
        prefix = strs[0]
        
        # Compare the prefix with each string in the list
        for s in strs[1:]:
            # Reduce the prefix length until it matches the start of `s`
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                # If the prefix becomes empty, return ""
                if not prefix:
                    return ""
        
        return prefix