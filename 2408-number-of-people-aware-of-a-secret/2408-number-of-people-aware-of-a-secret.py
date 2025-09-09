class Solution:
  def peopleAwareOfSecret(self, n: int, d: int, f: int) -> int:
    m = 10**9 + 7
    a = [0] * f
    a[0] = 1
    s = 0
    for i in range(1, n):
      if i - d >= 0: s += a[(i - d) % f]
      if i - f >= 0: s -= a[(i - f) % f]
      s %= m
      a[i % f] = s
    return sum(a) % m
