class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        cnt = [0] * n

        free = list(range(n))
        busy = []

        for s, e in meetings:
            i = 0
            while i < len(busy):
                if busy[i][0] <= s:
                    free.append(busy[i][1])
                    busy.pop(i)
                else:
                    i += 1

            free.sort()
            busy.sort()

            if free:
                r = free.pop(0)
                cnt[r] += 1
                busy.append((e, r))
            else:
                t, r = busy.pop(0)
                cnt[r] += 1
                busy.append((t + e - s, r))

        return cnt.index(max(cnt))
