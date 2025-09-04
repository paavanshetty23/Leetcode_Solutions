import heapq
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []

        for x, y in points:
            dist = -(x**2 + y**2)  # negate to simulate max-heap
            heapq.heappush(max_heap, (dist, x, y))

            if len(max_heap) > k:
                heapq.heappop(max_heap)  # remove farthest point

        return [[x, y] for (dist, x, y) in max_heap]
