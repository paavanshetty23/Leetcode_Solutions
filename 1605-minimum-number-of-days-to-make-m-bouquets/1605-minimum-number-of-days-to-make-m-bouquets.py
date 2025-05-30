from typing import List
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)

        if m * k > n:
            return -1

        def possible(day: int) -> bool:
            cnt = 0
            noofB = 0
            for i in range(n):
                if bloomDay[i] <= day:
                    cnt += 1
                else:
                    noofB += cnt // k
                    cnt = 0
            noofB += cnt // k
            return noofB >= m
        
        low = min(bloomDay)
        high = max(bloomDay)

        while low <= high:
            mid = (low + high) // 2
            if possible(mid):
                high = mid - 1
            else:
                low = mid + 1
        return low
            