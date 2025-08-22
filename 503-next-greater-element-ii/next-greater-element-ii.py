class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        stack =[]
        
        n = len(nums)
        res = [-1]* n

        for i in range(2*n-1,-1,-1):
            num = nums[i%n]

            while stack and stack[-1]<=num:
                stack.pop()

            if i < n:
                res[i]=stack[-1] if stack else -1
            stack.append(num)

        return [res[i] for i in range(n)]
        