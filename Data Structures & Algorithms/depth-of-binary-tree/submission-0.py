# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        depth = 1
        max_depth = 0
        stack = [(root, depth)]
        
        while stack:

            node, curr_depth = stack.pop()

            if not node.left and not node.right:
                max_depth = max(curr_depth, max_depth)

            if node.right:
                stack.append((node.right, curr_depth + 1))

            if node.left:
                stack.append((node.left, curr_depth + 1))

        return max_depth