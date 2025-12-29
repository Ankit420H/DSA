class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        from collections import defaultdict

        d = defaultdict(list)
        for s in allowed:
            d[s[:2]].append(s[2])

        bad = set()

        def f(r):
            if len(r) == 1:
                return True
            if r in bad:
                return False
            bad.add(r)

            def g(i, cur):
                if i + 1 == len(r):
                    return f(cur)
                for c in d[r[i:i+2]]:
                    if g(i + 1, cur + c):
                        return True
                return False

            return g(0, "")

        return f(bottom)
