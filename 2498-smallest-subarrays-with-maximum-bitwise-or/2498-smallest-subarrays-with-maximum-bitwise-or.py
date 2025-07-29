class Solution:
  def smallestSubarrays(self, nums: list[int]) -> list[int]:
    n = len(nums)
    ans = [1] * n
    bit = [n] * 30
    for i in range(n - 1, -1, -1):
      for j in range(30):
        if nums[i] >> j & 1:
          bit[j] = i
      far = i
      for j in range(30):
        if bit[j] < n:
          far = max(far, bit[j])
      ans[i] = far - i + 1
    return ans