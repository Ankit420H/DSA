class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        n = len(arr)
        ans = 0
        
        for i in range(n):
            for j in range(i, n):
                le = j - i + 1
                if le % 2 == 1:
                    s = 0
                    for k in range(i, j + 1):
                        s += arr[k]
                    ans += s
                    
        return ans
