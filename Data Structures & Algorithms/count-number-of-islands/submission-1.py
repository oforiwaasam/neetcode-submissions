class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols, count = len(grid), len(grid[0]), 0

        def dfs(r, c):
            
            # if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != '1':
            #     return
            
            queue = deque()
            grid[r][c] = '0'
            queue.append((r, c))

            while queue:
                row, col = queue.pop()
                directions = [[0, -1], [0, 1], [1, 0], [-1, 0]]

                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r) in range(rows) and (c) in range(cols) and grid[r][c] == '1':
                        queue.append((r, c))
                        grid[r][c] = '0'

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    count += 1
                    dfs(r, c)

        return count