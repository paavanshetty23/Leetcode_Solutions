from typing import List

class Solution:
    def _merge(self, arr: List[int], low: int, mid: int, high: int):
        temp = []
        left = low
        right = mid + 1

        while left <= mid and right <= high:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                right += 1

        while left <= mid:
            temp.append(arr[left])
            left += 1

        while right <= high:
            temp.append(arr[right])
            right += 1

        for i in range(low, high + 1):
            arr[i] = temp[i - low]

    def _countPairs(self, arr: List[int], low: int, mid: int, high: int) -> int:
        right = mid + 1
        cnt = 0
        for i in range(low, mid + 1):
            while right <= high and arr[i] > 2 * arr[right]:
                right += 1
            cnt += (right - (mid + 1))
        return cnt

    def _mergeSort(self, arr: List[int], low: int, high: int) -> int:
        cnt = 0
        if low >= high:
            return cnt
        mid = (low + high) // 2
        cnt += self._mergeSort(arr, low, mid)
        cnt += self._mergeSort(arr, mid + 1, high)
        cnt += self._countPairs(arr, low, mid, high)
        self._merge(arr, low, mid, high)
        return cnt

    def reversePairs(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        return self._mergeSort(nums, 0, n - 1)
