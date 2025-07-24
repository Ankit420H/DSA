class Solution:
    def minimumScore(self, nums: list[int], edges: list[list[int]]) -> int:
        n = len(nums)
        total = functools.reduce(operator.xor, nums)
        sub = nums[:]
        graph = [[] for _ in range(n)]
        child = [{i} for i in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(u, p):
            for v in graph[u]:
                if v == p:
                    continue
                x, c = dfs(v, u)
                sub[u] ^= x
                child[u] |= c
            return sub[u], child[u]

        dfs(0, -1)

        ans = math.inf
        for i in range(len(edges)):
            a, b = edges[i]
            if b in child[a]:
                a, b = b, a
            for j in range(i):
                c, d = edges[j]
                if d in child[c]:
                    c, d = d, c

                if c in child[a] and a != c:
                    vals = [sub[c], sub[a] ^ sub[c], total ^ sub[a]]
                elif a in child[c] and a != c:
                    vals = [sub[a], sub[c] ^ sub[a], total ^ sub[c]]
                else:
                    vals = [sub[a], sub[c], total ^ sub[a] ^ sub[c]]

                ans = min(ans, max(vals) - min(vals))

        return ans