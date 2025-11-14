class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        ar = 0
        while i < j:
            d = min(height[i], height[j])
            k = j - i
            ar = max(ar, d * k)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return ar
