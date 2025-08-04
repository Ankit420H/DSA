class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        ans = 0
        freq = defaultdict(int)
        l = 0

        for r, x in enumerate(fruits):
            freq[x] += 1
            while len(freq) > 2:
                freq[fruits[l]] -= 1
                if freq[fruits[l]] == 0:
                    del freq[fruits[l]]
                l += 1
            ans = max(ans, r - l + 1)
        return ans