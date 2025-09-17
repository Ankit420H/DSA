class FoodRatings:
    def __init__(self, foods: list[str], cuisines: list[str], ratings: list[int]):
        self.cm = defaultdict(lambda: SortedSet(key=lambda x: (-x[0], x[1])))
        self.fc = {}
        self.fr = {}
        for f, c, r in zip(foods, cuisines, ratings):
            self.cm[c].add((r, f))
            self.fc[f] = c
            self.fr[f] = r

    def changeRating(self, food: str, newRating: int) -> None:
        c = self.fc[food]
        r = self.fr[food]
        s = self.cm[c]
        s.remove((r, food))
        s.add((newRating, food))
        self.fr[food] = newRating

    def highestRated(self, cuisine: str) -> str:
        return self.cm[cuisine][0][1]
