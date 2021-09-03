class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        m, n = len(board), len(board[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        
        def dfs(position, word, visited):
            if not word:
                return True
            x, y = position
            if board[x][y] == word[0]:
                if len(word) == 1:
                    return True
                for p, q in directions:
                    nx, ny = x+p, y+q
                    if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                        visited[nx][ny] = True
                        ret = dfs((nx, ny), word[1:], visited)
                        if ret:
                            return True
                        visited[nx][ny] = False
            return False
                    
        
        for i in range(m):
            for j in range(n):
                visited[i][j] = True
                ret = dfs((i, j), word, visited) 
                if ret:
                    return True
                visited[i][j] = False
        
        return False