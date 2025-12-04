class Solution:
    def countCollisions(self, directions: str) -> int:
        d=directions
        l = 0
        r = len(d) - 1
        while l < len(d) and d[l] == 'L': l += 1
        while r >= 0 and d[r] == 'R': r -= 1
        return sum(x != 'S' for x in d[l:r+1])
