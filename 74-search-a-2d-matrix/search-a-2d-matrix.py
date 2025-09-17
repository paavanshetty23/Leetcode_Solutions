class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:


        def binarys(matrix,target):

            n = len(matrix)
            low,high = 0,n-1

            while low<=high:
                mid=(low+high)//2

                if matrix[mid]== target:
                    return True
                elif matrix[mid]<target:
                    low=mid+1
                else:
                    high= mid-1
            return False

        n=len(matrix)
        m= len(matrix[0])

        for i in range (n):
            if binarys(matrix[i],target):
                return True
        
        return False
        








        