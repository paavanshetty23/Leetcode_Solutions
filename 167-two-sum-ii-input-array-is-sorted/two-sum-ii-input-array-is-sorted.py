class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        n = len(numbers)

        for i in range(n):
            comp = target -numbers[i]
            low = i+1
            high =n-1

            while low<=high:
                mid = (low+high)//2

                if(numbers[mid]==comp):
                    return [i+1,mid+1]
                elif (numbers[mid]<comp):
                    low=mid+1
                else:
                    high =mid-1
        return []


            