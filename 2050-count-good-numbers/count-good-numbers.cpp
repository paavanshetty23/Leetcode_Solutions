class Solution {
public:
    const int MOD = 1e9 + 7;

    long long power(long long base, long long exp) {
        long long result = 1;
        while (exp > 0) {
            if (exp % 2 == 1)
                result = (result * base) % MOD;
            base = (base * base) % MOD;
            exp /= 2;
        }
        return result;
    }

    int countGoodNumbers(long long n) {
        long long even = (n + 1) / 2;  // positions 0, 2, 4...
        long long odd = n / 2;         // positions 1, 3, 5...

        long long good_even = power(5, even); // 5 choices at even indices
        long long good_odd = power(4, odd);   // 4 choices at odd indices

        return (good_even * good_odd) % MOD;
    }
};
