class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        h = sum(l*l for _, _, l in squares) / 2
        e = [(y, 1, l) for _, y, l in squares] + [(y + l, -1, l) for _, y, l in squares]
        e.sort()
        s = 0
        w = 0
        p = 0
        for y, t, l in e:
            d = w * (y - p)
            if s + d >= h:
                return p + (h - s) / w
            s += d
            w += t * l
            p = y