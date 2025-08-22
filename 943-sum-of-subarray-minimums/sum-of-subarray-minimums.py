class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        

        mod= (int)(1e9+7)
        n= len(arr)

        pse = [-1]*n
        stack =[]

        for i in range(n):
            while stack and arr[stack[-1]]>arr[i]:
                stack.pop()
            pse[i]=stack[-1] if stack else -1
            stack.append(i)
        
        nse =[n]*n
        stack =[]

        for i in range(n-1,-1,-1):
            while stack and arr[stack[-1]]>=arr[i]:
                stack.pop()
            nse[i]=stack[-1] if stack else n
            stack.append(i)
        
        ans=0

        for i in range(n):
            left = i -pse[i]
            right=nse[i]-i

            ans = (ans+arr[i]*left*right)%mod
        return ans
            

