class Solution:
    def matrixReshape(self, nums: list[list[int]], r: int, c: int) -> list[list[int]]:
        row_len = len(nums)
        col_len = len(nums[0])
        total_elements = row_len * col_len

        if r * c != total_elements:
            return nums

        ans = []
        flat_list = []

        for row in nums:
            for num in row:
                flat_list.append(num)

        index = 0
        for i in range(r):
            new_row = []
            for j in range(c):
                new_row.append(flat_list[index])
                index += 1
            ans.append(new_row)

        return ans
