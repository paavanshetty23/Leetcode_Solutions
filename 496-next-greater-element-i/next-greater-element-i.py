from collections import deque
from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums2)
        next_great = {}
        stack = deque()

        for i in range(n):
            while stack and nums2[stack[-1]] < nums2[i]:
                next_great[nums2[stack.pop()]] = nums2[i]
            stack.append(i)
        while stack:
            next_great[nums2[stack.pop()]] = -1

        res = []
        for num in nums1:
            res.append(next_great[num])
        return res