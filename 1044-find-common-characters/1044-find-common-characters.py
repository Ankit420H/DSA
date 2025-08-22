class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        freq = [0] * 26
        for ch in words[0]:
            freq[ord(ch) - ord('a')] += 1

        for word in words[1:]:
            temp = [0] * 26
            for ch in word:
                temp[ord(ch) - ord('a')] += 1
            for i in range(26):
                freq[i] = min(freq[i], temp[i])

        result = []
        for i in range(26):
            for _ in range(freq[i]):
                result.append(chr(i + ord('a')))

        return result
