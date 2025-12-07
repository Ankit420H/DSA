class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        M = 1000000007
        n = len(nums)
        dp = [0]*(n+1)
        ps = [0]*(n+1)
        dp[0] = 1
        ps[0] = 1
        
        mn = collections.deque()
        mx = collections.deque()
        
        l = 0
        
        for r in range(n):
            while mn and mn[-1] > nums[r]:
                mn.pop()
            mn.append(nums[r])
            
            while mx and mx[-1] < nums[r]:
                mx.pop()
            mx.append(nums[r])
            
            while mx[0] - mn[0] > k:
                if mn[0] == nums[l]:
                    mn.popleft()
                if mx[0] == nums[l]:
                    mx.popleft()
                l += 1
            
            if l == 0:
                dp[r+1] = ps[r] % M
            else:
                dp[r+1] = (ps[r] - ps[l-1] + M) % M
            
            ps[r+1] = (ps[r] + dp[r+1]) % M
        
        return dp[n]
