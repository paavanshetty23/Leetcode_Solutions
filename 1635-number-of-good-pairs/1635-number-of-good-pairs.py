class Solution:
    @staticmethod
    def numIdenticalPairs(nums):
        count_map = {}
        good_pairs = 0

        for num in nums:
            # If the number is already in the map, then we can form "count_map[num]" pairs with this new occurrence.
            if num in count_map:
                good_pairs += count_map[num]
                count_map[num] += 1
            else:
                count_map[num] = 1

        return good_pairs

# Example usage:
nums = [1, 2, 3, 1, 1, 3]
print(Solution.numIdenticalPairs(nums))  # Output: 4