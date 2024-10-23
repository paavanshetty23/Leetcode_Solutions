class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        vector<vector<int>> rows(9, vector<int>(9, 0));     
    vector<vector<int>> cols(9, vector<int>(9, 0));     
    vector<vector<int>> boxes(9, vector<int>(9, 0));    
    
    for (int i = 0; i < 9; ++i) {
        for (int j = 0; j < 9; ++j) {
            char c = board[i][j];
            if (c != '.') {
                int num = c - '1';  
                
                // Check the row
                if (rows[i][num]) return false;
                rows[i][num] = 1;
                
                // Check the column
                if (cols[j][num]) return false;
                cols[j][num] = 1;
                
                // Check the 3x3 subgrid
                int boxIndex = (i / 3) * 3 + (j / 3);
                if (boxes[boxIndex][num]) return false;
                boxes[boxIndex][num] = 1;
            }
        }
    }
    
    return true;
}

};