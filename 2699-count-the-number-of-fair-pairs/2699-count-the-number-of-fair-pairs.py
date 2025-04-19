class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        def count_pairs_less_than(target):
            count = 0
            left, right = 0, len(nums) - 1
            
            while left < right:
                if nums[left] + nums[right] > target:
                    right -= 1
                else:
                    count += right - left
                    left += 1
                    
            return count
        
        nums.sort()
        
        return count_pairs_less_than(upper) - count_pairs_less_than(lower - 1)