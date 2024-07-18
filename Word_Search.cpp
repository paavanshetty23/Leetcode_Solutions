// .79. Word Search
// Given an m x n grid of characters board and a string word, return true if word exists in the grid.
// The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        if(board.empty()) return false;
        int m = board.size(), n = board[0].size();
        for(int i = 0; i < m; i++)
            for(int j = 0; j < n; j++)
                if(board[i][j] == word[0] && BFS(board, i, j, m, n, 0, word)) return true;
        return false;
    }
    
    bool BFS(vector<vector<char>>& board, int r, int c, int m, int n, int len, string& word){
        if(len == word.size()) return true;
        if(r < 0 || c < 0 || r >= m || c >= n || board[r][c] == '#' || board[r][c] != word[len]) return false;
        char tmp = board[r][c];
        board[r][c] = '#';
        bool found =  BFS(board, r + 1, c, m, n, len + 1, word) || BFS(board, r, c + 1, m, n, len + 1, word) || BFS(board, r - 1, c, m, n, len + 1, word) || BFS(board, r, c - 1, m, n, len + 1, word);
        board[r][c] = tmp;
        return found;
    }
};
