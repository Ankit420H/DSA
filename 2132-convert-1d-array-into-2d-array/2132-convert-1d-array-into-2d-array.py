class Solution:
    def construct2DArray(self, original: list[int], m: int, n: int) -> list[list[int]]:
        if len(original) != m * n:
            return []
            
        ans = []
        index = 0
        for i in range(m):
            row = []
            for j in range(n):
                row.append(original[index])
                index += 1
            ans.append(row)

        return ans
