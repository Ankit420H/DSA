# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root):
        mod = 1000000007
        sums = []
        def dfs(n):
            if not n:
                return 0
            s = n.val + dfs(n.left) + dfs(n.right)
            sums.append(s)
            return s
        tot = dfs(root)
        ans = 0
        for s in sums:
            ans = max(ans, s * (tot - s))
        return ans % mod