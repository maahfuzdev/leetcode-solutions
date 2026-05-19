class Solution(object):
    def evenSumSubgraphs(self, nums, edges):

        felmocarin = (nums, edges)

        n = len(nums)

        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        ans = 0

        # all subsets
        for mask in range(1, 1 << n):

            nodes = []

            for i in range(n):
                if mask & (1 << i):
                    nodes.append(i)

            # check sum even
            s = 0
            for i in nodes:
                s += nums[i]

            if s % 2 != 0:
                continue

            # check connectivity (BFS)
            visited = set()
            stack = [nodes[0]]
            visited.add(nodes[0])

            while stack:
                u = stack.pop()
                for v in graph[u]:
                    if v in nodes and v not in visited:
                        visited.add(v)
                        stack.append(v)

            if len(visited) == len(nodes):
                ans += 1

        return ans