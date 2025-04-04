class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int xorlist= nums[0] ;
        for ( int i =1 ; i<nums.size();i++){
            xorlist = xorlist ^ nums[i];

        }
        return xorlist;
    }
};