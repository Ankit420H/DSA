class Solution:
  def maxSubsequence(self, nums: list[int], k: int) -> list[int]:
    temp = nums[:]

    temp.sort(reverse=True)
    top_k = temp[:k]

    count = []
    for num in top_k:
      count.append(num)

    result = []
    for num in nums:
      if num in count:
        result.append(num)
        count.remove(num) 
        if len(result) == k:
          break

    return result
