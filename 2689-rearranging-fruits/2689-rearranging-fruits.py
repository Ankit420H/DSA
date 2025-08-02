from collections import Counter

class Solution:
    def minCost(self, basket1: list[int], basket2: list[int]) -> int:
        cnt = Counter(basket1)
        cnt.subtract(basket2)
        
        lst = []
        for x in cnt:
            if cnt[x] % 2 != 0:
                return -1
            for _ in range(abs(cnt[x]) // 2):
                lst.append(x)

        lst.sort()
        mn = min(min(basket1), min(basket2))
        ans = 0
        for i in range(len(lst) // 2):
            ans += min(lst[i], 2 * mn)

        return ans
