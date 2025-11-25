class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 10 not in {1, 3, 7, 9}:
            return -1
        s = set()
        r = 0
        for i in range(1, k + 1):
            r = (r * 10 + 1) % k
            if r == 0:
                return i
            if r in s:
                return -1
            s.add(r)
        return -1