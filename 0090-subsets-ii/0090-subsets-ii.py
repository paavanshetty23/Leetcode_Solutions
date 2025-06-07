class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        res = set()

        def func(index:int,ds:List[int]):
            if index == len(nums):
                ds.sort()
                res.add(tuple(ds))
                return
            ds.append(nums[index])
            func(index+1,ds)
            ds.pop()
            func(index+1,ds)
        func(0,[])

        for it in res:
            ans.append(list(it))
        return ans