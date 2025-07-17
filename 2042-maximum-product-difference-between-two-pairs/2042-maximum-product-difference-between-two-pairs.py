class Solution:
  def maxProductDifference(self, nums: list[int]) -> int:
    ma1 = float('-inf')
    ma2 = float('-inf')
    mi1 = float('inf')
    mi2 = float('inf')

    for num in nums:
      if num > ma1:
        ma2 = ma1
        ma1 = num
      elif num > ma2:
        ma2 = num

      if num < mi1:
        mi2 = mi1
        mi1 = num
      elif num < mi2:
        mi2 = num

    return ma1 * ma2 - mi1 * mi2
