# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def hei(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            lefty=hei(root.left)
            if lefty==-1:
                return -1
            righty=hei(root.right)
            if righty==-1:
                return -1
            if abs(lefty-righty)>1:
                return -1
            return 1+max(lefty,righty)
        return hei(root)!=-1
            