class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge(l, r):
            cnt = 0
            j = 0
            for i in range(len(l)):
                while j < len(r) and l[i] > 2 * r[j]:
                    j += 1
                cnt += j
            return cnt

        def sort(a):
            if len(a) <= 1:
                return a, 0
            m = len(a) // 2
            l, c1 = sort(a[:m])
            r, c2 = sort(a[m:])
            c3 = merge(l, r)

            i = j = 0
            res = []
            while i < len(l) and j < len(r):
                if l[i] <= r[j]:
                    res.append(l[i])
                    i += 1
                else:
                    res.append(r[j])
                    j += 1
            res.extend(l[i:])
            res.extend(r[j:])

            return res, c1 + c2 + c3

        _, ans = sort(nums)
        return ans
