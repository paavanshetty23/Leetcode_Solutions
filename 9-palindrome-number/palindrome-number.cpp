class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0) return false; 

        int temp = x, reversed = 0;
        
        while (temp != 0) {
            int digit = temp % 10;
            if (reversed > (INT_MAX - digit) / 10) return false; 

            reversed = reversed * 10 + digit;
            temp /= 10;
        }
        
        return reversed == x;
    }
};
