class Solution {
public:
    int longestConsecutive(const std::vector<int>& nums) {
        if (nums.empty()) return 0;

        std::unordered_set<int> numSet(nums.begin(), nums.end()); 
        int longestStreak = 0;

        for (int num : numSet) {
           
            if (numSet.find(num - 1) == numSet.end()) {
                int currentNum = num;
                int currentStreak = 1;

                
                while (numSet.find(currentNum + 1) != numSet.end()) {
                    currentNum += 1;
                    currentStreak += 1;
                }

               
                longestStreak = std::max(longestStreak, currentStreak);
            }
        }

        return longestStreak;
    }
};