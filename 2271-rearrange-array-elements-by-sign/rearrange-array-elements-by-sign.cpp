class Solution {
public:
    vector<int> rearrangeArray(vector<int>& nums) {
        int n = nums.size();
        vector<int> a(n,0);
        int pos = 0 , neg =1;
      for ( int i = 0 ; i<n ;i++){
        if (nums[i]<0){
            a[neg]=nums[i];
            neg+=2;
        }
        else{
            a[pos]=nums[i];
            pos+=2;
        }


      }
      nums.swap(a);
      return nums;
    }
};