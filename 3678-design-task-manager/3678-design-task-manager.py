class TaskManager:
    def __init__(self, lst: list[list[int]]):
        self.h = []
        self.m = {}
        for u, t, p in lst:
            self.m[t] = (u, p)
            heapq.heappush(self.h, (-p, -t, t))

    def add(self, u: int, t: int, p: int):
        self.m[t] = (u, p)
        heapq.heappush(self.h, (-p, -t, t))

    def edit(self, t: int, p: int):
        u, _ = self.m[t]
        self.m[t] = (u, p)
        heapq.heappush(self.h, (-p, -t, t))

    def rmv(self, t: int):
        if t in self.m:
            del self.m[t]

    def execTop(self) -> int:
        while self.h:
            a, b, t = self.h[0]
            cur = self.m.get(t)
            if cur is None or cur[1] != -a:
                heapq.heappop(self.h)
                continue
            heapq.heappop(self.h)
            u = self.m[t][0]
            del self.m[t]
            return u
        return -1
