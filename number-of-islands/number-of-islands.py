class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # use dfs to mark the visited nodes
        # number of sources is the number of islands
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        m, n = len(grid), len(grid[0])
        
        def dfs(node, visited):
            x, y = node
            for p, q in directions:
                nx, ny = x + p, y + q
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == '1' and not visited[nx][ny]:
                    visited[nx][ny] = True
                    dfs((nx, ny), visited)
        
        visited = [[False for _ in range(n)] for _ in range(m)]
        res = 0
        for row in range(m):
            for col in range(n):
                if not visited[row][col] and grid[row][col] == '1':
                    visited[row][col] = True
                    dfs((row, col), visited)
                    res += 1
                    
                    
        return res
                    