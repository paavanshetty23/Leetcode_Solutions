class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int n= nums.size();
        map<int , int> hm;
        for (auto num:nums){
            hm[num]++;
        }
        for (auto it : hm){
            if (it.second > (n/2)){
                return it.first;
            }        
        }
        return 0;
    }
};