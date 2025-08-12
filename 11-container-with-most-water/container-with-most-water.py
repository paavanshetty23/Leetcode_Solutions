class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        amt=0
        res=0
        l,r=0,n-1

        while l<r:
            amt = min(height[l],height[r])*(r-l)
            res = max(amt,res)

            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return res


        