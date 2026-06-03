# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        queue = deque()
        queue.append(root)
        result = []

        while queue: # [2,3]
            currentLevel = [] 

            for _ in range(len(queue)): # 2
                currentNode = queue.popleft() # 3
                currentLevel.append(currentNode.val) # [2,3]

                if currentNode.left:
                    queue.append(currentNode.left) # [4,5,6]

                if currentNode.right:
                    queue.append(currentNode.right) # [4,5,6,7]

            result.append(currentLevel) # [[1], [2,3]]

        return result
                
            

