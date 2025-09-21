from sortedcontainers import SortedList
import collections

class MovieRentingSystem:
    def __init__(self, n: int, entries: list[list[int]]):
        self.unrented = collections.defaultdict(SortedList)
        self.price_map = {}
        self.rented = SortedList()
        for s, m, p in entries:
            self.unrented[m].add((p, s))
            self.price_map[(s, m)] = p

    def search(self, m: int) -> list[int]:
        return [s for _, s in self.unrented[m][:5]]

    def rent(self, s: int, m: int) -> None:
        p = self.price_map[(s, m)]
        self.unrented[m].remove((p, s))
        self.rented.add((p, s, m))

    def drop(self, s: int, m: int) -> None:
        p = self.price_map[(s, m)]
        self.unrented[m].add((p, s))
        self.rented.remove((p, s, m))

    def report(self) -> list[list[int]]:
        return [[s, m] for _, s, m in self.rented[:5]]
