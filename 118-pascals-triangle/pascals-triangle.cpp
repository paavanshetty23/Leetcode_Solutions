class Solution {
public:
    vector<int> combination(int n) {
        long long res = 1;
        vector<int> row;
        row.push_back(1); 
        for (int i = 1; i <= n; i++) {
            res = res * (n - i + 1) / i;
            row.push_back((int)(res));
        }
        return row;
    }

    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> res;
        for (int i = 0; i < numRows; i++) {
            res.push_back(combination(i));
        }
        return res;
    }
};
