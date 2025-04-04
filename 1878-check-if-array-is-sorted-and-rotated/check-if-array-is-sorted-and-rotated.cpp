class Solution {
public:
    bool check(vector<int>& nums) {
        int n = nums.size();
   
    vector<int> combined(nums.begin(), nums.end());
    combined.insert(combined.end(), nums.begin(), nums.end());
    for (int i = 0; i < n; i++) {
        bool isSorted = true;
        for (int j = i; j < i + n - 1; j++) {
            if (combined[j] > combined[j + 1]) {
                isSorted = false;
                break;
            }
        }
        if (isSorted) return true;
    }
    return false;
}

      
};