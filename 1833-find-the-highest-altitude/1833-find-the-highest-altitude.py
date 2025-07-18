class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        s = [0]
        for i in gain:
            s.append(s[-1] + i)
        return max(s)
