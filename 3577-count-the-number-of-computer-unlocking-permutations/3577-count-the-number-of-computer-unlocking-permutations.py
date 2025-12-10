class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        m = 10**9 + 7
        for i in range(1, len(complexity)):
            if complexity[i] <= complexity[0]:
                return 0
        r = 1
        for i in range(1, len(complexity)):
            r = (r * i) % m
        return r
