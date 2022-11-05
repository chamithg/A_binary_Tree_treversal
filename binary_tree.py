# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        output =[]
        
        

        
        def rec(node):
            
            if node!= None:
                if node.left:
                    rec(node.left)
                output.append(node.val)

                if node.right:
                    rec(node.right)
            
                
        rec(root)
        return(output)
            
                
        