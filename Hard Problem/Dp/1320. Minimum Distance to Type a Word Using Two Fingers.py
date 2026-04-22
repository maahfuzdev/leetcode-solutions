class Solution:
    def minimumDistance(self, word):
        # build coordinates for A-Z
        pos = {}
        for i in range(26):
            pos[i] = (i // 6, i % 6)

        def dist(a, b):
            if a == 26:  # free finger
                return 0
            x1, y1 = pos[a]
            x2, y2 = pos[b]
            return abs(x1 - x2) + abs(y1 - y2)

        # dp state: (finger1, finger2) -> cost
        dp = {(26, 26): 0}

        for ch in word:
            k = ord(ch) - ord('A')
            new_dp = {}

            for (i, j), cost in dp.items():
                # move finger 1
                ni, nj = k, j
                if ni > nj:
                    ni, nj = nj, ni
                new_dp[(ni, nj)] = min(
                    new_dp.get((ni, nj), float('inf')),
                    cost + dist(i, k)
                )

                # move finger 2
                ni, nj = i, k
                if ni > nj:
                    ni, nj = nj, ni
                new_dp[(ni, nj)] = min(
                    new_dp.get((ni, nj), float('inf')),
                    cost + dist(j, k)
                )

            dp = new_dp

        return min(dp.values())