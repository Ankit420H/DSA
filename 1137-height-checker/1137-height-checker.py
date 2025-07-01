class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count=0
        e=sorted(heights)
        for i in range(len(e)):
            if e[i]!=heights[i]:
                count+=1
        return count