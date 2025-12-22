class Solution:
    def fillCups(self, amount: List[int]) -> int:
        s=sum(amount)
        return max(max(amount),(s+1)//2)
