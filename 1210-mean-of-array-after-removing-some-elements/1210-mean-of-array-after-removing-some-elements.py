class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        n = len(arr)
        k = int(n * 0.05)

        arr = arr[k:n - k]

        s = 0
        for i in range(len(arr)):
            s += arr[i]
        s = s / len(arr)

        return round(s, 5)
