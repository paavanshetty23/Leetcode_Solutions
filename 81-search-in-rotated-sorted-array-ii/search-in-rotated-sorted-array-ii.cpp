class Solution {
public:
    bool search(vector<int>& nums, int target) {
        int n = nums.size();
        int pos = -1;

        for (int i = 0; i < n - 1; i++) {
            if (nums[i] > nums[i + 1]) {
                pos = i;
                break;
            }
        }

        int low, high, mid;

        if (pos == -1) {
            low = 0;
            high = n - 1;
        } else if (target >= nums[pos + 1] && target <= nums[n - 1]) {
            low = pos + 1;
            high = n - 1;
        } else {
            low = 0;
            high = pos;
        }

        while (low <= high) {
            mid = (low + high) / 2;
            if (nums[mid] == target) return true;
            else if (nums[mid] < target) low = mid + 1;
            else high = mid - 1;
        }

        return false;
    }
};
