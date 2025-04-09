#include <vector>
#include <map>
using namespace std;

class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        int n = nums.size();
        vector<int> res;
        map<int, int> freq;
        for (int num : nums) {
            freq[num]++;
        }

        for (auto& pair : freq) {
            if (pair.second > n / 3) {
                res.push_back(pair.first);
            }
        }

        return res;
    }
};
