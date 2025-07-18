class Solution:
    def finalValueAfterOperations(self, a: list[str]) -> int:
        return sum(1 if '+' in i else -1 for i in a)
