class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        pos2 = {}
        for i in range(n):
            pos2[nums2[i]] = i
        positions = [pos2[nums1[i]] for i in range(n)]
    
        bit = [0] * (n + 1)
        
        def update(idx, val):
            idx += 1 
            while idx <= n:
                bit[idx] += val
                idx += idx & -idx
        
        def query(idx):
            idx += 1 
            result = 0
            while idx > 0:
                result += bit[idx]
                idx -= idx & -idx
            return result
        
        result = 0
        
        smaller_left = [0] * n
        
        for i in range(n):
            smaller_left[i] = query(positions[i] - 1)  
            update(positions[i], 1) 
        bit = [0] * (n + 1)
        
        for i in range(n-1, -1, -1):
            larger_right = query(n - 1) - query(positions[i]) 
            result += smaller_left[i] * larger_right 
            update(positions[i], 1) 
        return result