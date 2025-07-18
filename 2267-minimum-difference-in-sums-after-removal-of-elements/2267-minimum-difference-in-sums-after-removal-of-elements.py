class Solution:
    def minimumDifference(self, nums: list[int]) -> int:
        n = len(nums) // 3
        total = len(nums)
        ans = math.inf
        left_sum = 0
        right_sum = 0
        left_heap = []
        right_heap = []
        left_min_sum = [0] * total

        for i in range(2 * n):
            heapq.heappush(left_heap, -nums[i])
            left_sum += nums[i]
            if len(left_heap) > n:
                left_sum += heapq.heappop(left_heap)
            if len(left_heap) == n:
                left_min_sum[i] = left_sum

        for i in range(total - 1, n - 1, -1):
            heapq.heappush(right_heap, nums[i])
            right_sum += nums[i]
            if len(right_heap) > n:
                right_sum -= heapq.heappop(right_heap)
            if len(right_heap) == n:
                ans = min(ans, left_min_sum[i - 1] - right_sum)

        return ans
