class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        import heapq
        c = [0] * n
        meetings.sort()
        occ = []
        avail = [i for i in range(n)]
        heapq.heapify(avail)

        for s, e in meetings:
            while occ and occ[0][0] <= s:
                heapq.heappush(avail, heapq.heappop(occ)[1])
            if avail:
                r = heapq.heappop(avail)
                c[r] += 1
                heapq.heappush(occ, (e, r))
            else:
                ns, r = heapq.heappop(occ)
                c[r] += 1
                heapq.heappush(occ, (ns + (e - s), r))

        return c.index(max(c))