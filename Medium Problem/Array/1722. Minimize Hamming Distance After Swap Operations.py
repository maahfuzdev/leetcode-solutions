from collections import defaultdict, Counter

class Solution:
    def minimumHammingDistance(self, source, target, allowedSwaps):

        n = len(source)

        # ---------- DSU ----------
        parent = list(range(n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            pa, pb = find(a), find(b)
            if pa != pb:
                parent[pb] = pa

        # build groups
        for a, b in allowedSwaps:
            union(a, b)

        # ---------- group indices ----------
        groups = defaultdict(list)

        for i in range(n):
            groups[find(i)].append(i)

        # ---------- calculate mismatch ----------
        mismatch = 0

        for indices in groups.values():

            freq = Counter()

            # count source values
            for i in indices:
                freq[source[i]] += 1

            # try matching target
            for i in indices:
                if freq[target[i]] > 0:
                    freq[target[i]] -= 1
                else:
                    mismatch += 1

        return mismatch