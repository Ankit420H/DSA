class Seg:
    def __init__(self, xs):
        self.xs = xs
        self.n = len(xs) - 1
        self.c = [0] * (4 * self.n)
        self.w = [0] * (4 * self.n)

    def add(self, i, j, v):
        self._add(0, 0, self.n - 1, i, j, v)

    def _add(self, k, l, r, i, j, v):
        if j <= self.xs[l] or self.xs[r + 1] <= i:
            return
        if i <= self.xs[l] and self.xs[r + 1] <= j:
            self.c[k] += v
        else:
            m = (l + r) // 2
            self._add(k * 2 + 1, l, m, i, j, v)
            self._add(k * 2 + 2, m + 1, r, i, j, v)
        if self.c[k] > 0:
            self.w[k] = self.xs[r + 1] - self.xs[l]
        elif l == r:
            self.w[k] = 0
        else:
            self.w[k] = self.w[k * 2 + 1] + self.w[k * 2 + 2]

    def width(self):
        return self.w[0]


class Solution:
    def separateSquares(self, squares):
        ev = []
        xs = set()

        for x, y, l in squares:
            ev.append((y, 1, x, x + l))
            ev.append((y + l, -1, x, x + l))
            xs.add(x)
            xs.add(x + l)

        ev.sort()
        xs = sorted(xs)

        half = self.area(ev, xs) / 2
        seg = Seg(xs)

        a = 0
        py = ev[0][0]

        for y, d, xl, xr in ev:
            w = seg.width()
            g = w * (y - py)
            if a + g >= half:
                return py + (half - a) / w
            a += g
            seg.add(xl, xr, d)
            py = y

    def area(self, ev, xs):
        seg = Seg(xs)
        a = 0
        py = ev[0][0]

        for y, d, xl, xr in ev:
            a += seg.width() * (y - py)
            seg.add(xl, xr, d)
            py = y

        return a
