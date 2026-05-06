# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode], res: int) -> tuple[int, int]:
            if not node:
                return (res, 0)

            l_res, left_gain = dfs(node.left, res)
            r_res, right_gain = dfs(node.right, l_res)

            left_gain  = max(left_gain,  0)
            right_gain = max(right_gain, 0)

            # Best path using both children through this node
            new_res = max(r_res, node.val + left_gain + right_gain)
            # Best downward path to propagate up
            new_gain = node.val + max(left_gain, right_gain)

            return (new_res, new_gain)

        if not root:
            return 0
        # Initialize res with root.val so we handle all-negative trees
        res, _ = dfs(root, root.val)
        return res
