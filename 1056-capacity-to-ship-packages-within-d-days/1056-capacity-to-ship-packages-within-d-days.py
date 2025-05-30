class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low,high=max(weights),sum(weights)

        def findday(weights,cap):
            day,load=1,0
            n= len(weights)
            for i in range(n):
                if load+weights[i] > cap:
                    day+=1
                    load= weights[i]
                else:
                    load+=weights[i]
            return day


        while low<=high:
            mid = (low+high)//2
            nod = findday(weights,mid)
            if nod<=days:
                high=mid-1
            else:
                low= mid+1
        return low
