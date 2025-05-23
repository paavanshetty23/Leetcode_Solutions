from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        ds = []
        n = len(candidates)
        def combi(index : int,target:int):
            if index == n:
                if target == 0:
                    ans.append(ds[:])
                return
            if candidates[index] <= target:
                ds.append(candidates[index])
                combi(index,target-candidates[index])
                ds.pop()
            combi(index+1,target)
        combi(0,target)
        return ans