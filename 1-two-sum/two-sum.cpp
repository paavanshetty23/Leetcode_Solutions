class Solution {
public:
    std::vector<int> twoSum(const std::vector<int>& nums, int target) {
        std::unordered_map<int, int> numMap;
        
        for (int i = 0; i < nums.size(); ++i) {
            int complement = target - nums[i];
            
           
            if (numMap.find(complement) != numMap.end()) {
                return {numMap[complement], i}; 
            }
            
            // Add current number to the map
            numMap[nums[i]] = i;
        }
        
        return {}; 
    }
};