class Solution:
    def spellchecker(self, wordlist: list[str], queries: list[str]) -> list[str]:
        def lowerKey(w): return w.lower()
        def vowelKey(w): return ''.join('*' if c in 'aeiou' else c for c in w.lower())

        words = set(wordlist)
        lower, vowel = {}, {}

        for w in wordlist:
            lw, vw = lowerKey(w), vowelKey(w)
            if lw not in lower: lower[lw] = w
            if vw not in vowel: vowel[vw] = w

        ans = []
        for q in queries:
            if q in words:
                ans.append(q)
            elif lowerKey(q) in lower:
                ans.append(lower[lowerKey(q)])
            elif vowelKey(q) in vowel:
                ans.append(vowel[vowelKey(q)])
            else:
                ans.append('')
        return ans
