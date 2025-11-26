import heapq

class Solution:
    def getFinalState(self, nums, k, m):
        if m == 1:
            return nums
        MOD = 1000000007
        n = len(nums)
        mx = max(nums)
        h = [(nums[i], i) for i in range(n)]
        heapq.heapify(h)
        while k > 0 and h[0][0] * m <= mx:
            v, j = heapq.heappop(h)
            v *= m
            heapq.heappush(h, (v, j))
            k -= 1
        a = sorted(h)
        t = k // n
        r = k % n
        p = pow(m, t, MOD)
        for i in range(n):
            v, j = a[i]
            v = (v * p) % MOD
            a[i] = (v, j)
        for i in range(r):
            v, j = a[i]
            v = (v * m) % MOD
            a[i] = (v, j)
        out = [0] * n
        for v, j in a:
            out[j] = v
        return out
