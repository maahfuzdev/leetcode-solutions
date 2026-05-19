from collections import deque

class Solution(object):
    def hasValidPath(self, grid):

        m, n = len(grid), len(grid[0])

        directions = {
            1: [(0,-1),(0,1)],
            2: [(-1,0),(1,0)],
            3: [(0,-1),(1,0)],
            4: [(0,1),(1,0)],
            5: [(0,-1),(-1,0)],
            6: [(0,1),(-1,0)]
        }

        opposite = {
            (0,-1):(0,1),
            (0,1):(0,-1),
            (-1,0):(1,0),
            (1,0):(-1,0)
        }

        queue = deque([(0,0)])
        visited = set([(0,0)])

        while queue:
            r,c = queue.popleft()

            if (r,c) == (m-1,n-1):
                return True

            for dr,dc in directions[grid[r][c]]:
                nr,nc = r+dr, c+dc

                if 0<=nr<m and 0<=nc<n and (nr,nc) not in visited:

                    if opposite[(dr,dc)] in directions[grid[nr][nc]]:
                        visited.add((nr,nc))
                        queue.append((nr,nc))

        return False