class Solution:
    def bestClosingTime(self, customers: str) -> int:
        a = p = m = 0
        for i, c in enumerate(customers):
            p += 1 if c == 'Y' else -1
            if p > m:
                m = p
                a = i + 1
        return a
