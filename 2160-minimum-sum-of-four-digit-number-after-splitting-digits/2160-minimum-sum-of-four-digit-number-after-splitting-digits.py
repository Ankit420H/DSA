class Solution:
    def minimumSum(self, num: int) -> int:
        l = sorted(str(num))
        return int(l[0] + l[2]) + int(l[1] + l[3])
