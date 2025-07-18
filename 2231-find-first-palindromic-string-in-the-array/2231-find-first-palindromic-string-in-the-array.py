class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for i in words:
            if list(i)==list(reversed(i)):
                return i
        else:
            return ""
