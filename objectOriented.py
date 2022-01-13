class TreeNode(object):
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

x = TreeNode(1)
y = TreeNode(2)
z = TreeNode(3)

x.left = y
x.right = z



class Solution:

    def invertTree(self, root):
       
        if root == None:
            return None
        
        r = self.invertTree(root.right)
        l = self.invertTree(root.left) 
        
        root.left = r
        root.right = l
        
        return root
        

solution = Solution()
print(solution.invertTree(x).right.val)


    
    
    
