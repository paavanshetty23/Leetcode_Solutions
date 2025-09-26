class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        n = len(heights)
        st = []
        res = 0

        for i in range(n):

            while st and heights[st[-1]]>=heights[i]:

                top =st.pop()

                width = i if not st else i-st[-1]-1

                res = max(res,heights[top]*width)
            st.append(i)

        while st:
                top =st.pop()

                width = n if not st else n-st[-1]-1

                res = max(res,heights[top]*width)

        return res
