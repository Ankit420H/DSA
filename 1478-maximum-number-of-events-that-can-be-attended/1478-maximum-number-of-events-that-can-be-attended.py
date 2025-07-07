class Solution:
  def maxEvents(self, events: list[list[int]]) -> int:
    import heapq

    events.sort()
    minHeap = []
    i = 0
    d = 0
    ans = 0

    while i < len(events) or minHeap:
      if not minHeap:
        d = events[i][0]
      while i < len(events) and events[i][0] == d:
        heapq.heappush(minHeap, events[i][1])
        i += 1
      heapq.heappop(minHeap)
      ans += 1
      d += 1
      while minHeap and minHeap[0] < d:
        heapq.heappop(minHeap)

    return ans
