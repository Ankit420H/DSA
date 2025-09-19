class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        t = 0
        d = {}
        for c in chars:
            d[c] = d.get(c, 0) + 1
        for w in words:
            x = d.copy()
            ok = True
            for c in w:
                if c not in x or x[c] == 0:
                    ok = False
                    break
                x[c] -= 1
            if ok:
                t += len(w)
        return t
