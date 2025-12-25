class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        h=happiness
        h.sort(reverse=True)
        s=0
        for i in range(k):
            if h[i]-i>0:
                s+=h[i]-i
        return s