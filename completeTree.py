# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        def calculateDepth(node):
            d = 0
            while(node.left):
                d+=1
                node = node.left
            return d
        def checkExistence(node,index,d):
            left = 0
            right = 2**d - 1            
            while(d):
                m = (left+right)/2
                if index<=m:
                    if node.left:
                        right = m
                        node = node.left
                        d-=1 
                    else:
                        return False
                else:                    
                    if node.right:
                        left = m+1
                        node = node.right
                        d-=1 
                    else:
                        return False
            return node
        
        if not root:
            return 0
        d = calculateDepth(root)

        left = 0
        right = 2**d-1
                
        while(left <= right):
            m = (left+right)//2
            if checkExistence(root,m,d):
                left = m+1
            else:
                right = m-1
        
        
        ans = 2**d-1 + left
        return ans