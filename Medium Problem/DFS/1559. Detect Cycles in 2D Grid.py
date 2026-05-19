class Solution(object):
    def containsCycle(self, grid):
        m, n = len(grid), len(grid[0])
        visited = [[False]*n for _ in range(m)]

        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        def dfs(r, c, pr, pc, char):
            if visited[r][c]:
                return True

            visited[r][c] = True

            for dr, dc in directions:
                nr, nc = r+dr, c+dc

                # boundary check
                if 0 <= nr < m and 0 <= nc < n:

                    # same character check
                    if grid[nr][nc] != char:
                        continue

                    # don't go back to parent
                    if nr == pr and nc == pc:
                        continue

                    if dfs(nr, nc, r, c, char):
                        return True

            return False

        # start DFS from every cell
        for i in range(m):
            for j in range(n):
                if not visited[i][j]:
                    if dfs(i, j, -1, -1, grid[i][j]):
                        return True

        return False  