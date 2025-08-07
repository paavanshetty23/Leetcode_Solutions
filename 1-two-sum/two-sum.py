class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        maps = {}


        for key,val in enumerate(nums):
             comp = target - val
             if comp in maps:
                return [maps[comp],key]
             maps[val]=key

        return []
            
            

            
        