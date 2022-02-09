class Solution {
public:
    
    bool recur(vector<vector<char>>& board, string& word, int i, int j, int n){
        if (word.size() == n){
            return true;
        }
        
        if (i < 0 || j < 0 || i >= board.size() || j >= board[0].size() || board[i][j] != word[n])
            return false;
        
        board[i][j] = '0';
        
        bool doesExist = recur(board, word, i+1, j, n+1) ||
                         recur(board, word, i-1, j, n+1) ||
                         recur(board, word, i, j+1, n+1) || 
                         recur(board, word, i, j-1, n+1);
        
        board[i][j] = word[n];
        
        return doesExist;
    }
    
    bool exist(vector<vector<char>>& board, string word) {
        /*
        DFS recursively check if substring exists
        check all four directions
        */
        for(int i = 0; i < board.size(); i++){
            for(int j = 0; j < board[0].size(); j++){
                if(board[i][j] == word[0] && recur(board, word, i, j, 0))
                    return true;
            }
        }
        
        return false;
        
    }
};